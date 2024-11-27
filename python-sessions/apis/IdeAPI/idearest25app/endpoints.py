import json

import bcrypt
from django.http import JsonResponse
from django.template.base import Token
from django.views.decorators.csrf import csrf_exempt
import secrets
from .models import UserSession, Category, Idea, Comment
from idearest25app.models import CustomUser


def health_check(request):
    http_response = {"is_living": True}
    return JsonResponse(http_response)

@csrf_exempt
def users(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Unsupported HTTP method'}, status=405)
    try:
        body_json = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

        # Validar presencia de parámetros
    required_params = ['username', 'useremail', 'password']
    if not all(param in body_json for param in required_params):
        return JsonResponse({'error': 'Missing parameter'}, status=400)

    # Extraer parámetros
    json_username = body_json['username']
    json_email = body_json['useremail']
    json_password = body_json['password']
    if '@' not in json_email or len(json_email) < 7:
        return JsonResponse({'error': 'Invalid email'}, status=400)
    if CustomUser.objects.filter(e_mail=json_email).exists():
        return JsonResponse({'error': 'Already registered'}, status=409)
    salted_and_hashed_pass = bcrypt.hashpw(json_password.encode('utf8'), bcrypt.gensalt()).decode('utf8')
    user_object = CustomUser(e_mail=json_email, username=json_username, encrypted_password=salted_and_hashed_pass)
    user_object.save()
    return JsonResponse({"is_registered": True}, status=201)
@csrf_exempt
def sessions(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'HTTP method unsupported'}, status=405)
    try:
        body_json = json.loads(request.body)
        json_email = body_json['login_email']
        json_password = body_json['login_password']
    except (KeyError, json.JSONDecodeError):
        return JsonResponse({'error': 'Missing parameter in body'}, status=400)
    try:
        db_user = CustomUser.objects.get(e_mail=json_email)
    except CustomUser.DoesNotExist:
        return JsonResponse({'error': 'User does not exist'}, status=404)
    if bcrypt.checkpw(json_password.encode('utf8'), db_user.encrypted_password.encode('utf8')):
        random_token = secrets.token_hex(10)
        session = UserSession(creator=db_user, token=random_token)
        session.save()
        return JsonResponse({"token": random_token}, status=201)
    else:
        return JsonResponse({'error': 'Invalid password'}, status=401)

@csrf_exempt
def categories(request):
    if request.method != 'GET':
        return JsonResponse({'error': 'HTTP method unsupported'}, status=405)
    categories = Category.objects.all().values('id', 'title')
    json_response = [
        {"category_id": category['id'], "category_name": category['title']}
        for category in categories
    ]
    return JsonResponse(json_response, safe=False, status=200)

@csrf_exempt
def ideas(request, category_id):
    if request.method == 'POST':
        try:
            category = Category.objects.get(id=category_id)
            body_json = json.loads(request.body)
            json_title = body_json['new_idea_title']
            json_description = body_json['description']
            idea = Idea()
            # ¿De quién es la idea?
            authenticated_user = __get_request_user(request)
            if authenticated_user is None:
                return JsonResponse({"error": "Authentication not valid"}, status=401)
            idea.user = authenticated_user
            idea.title = json_title
            idea.description = json_description
            idea.category = category
            idea.save()
            return JsonResponse({"success": True}, status=201)
        except KeyError:
            return JsonResponse({"error": "You are missing a parameter"}, status=400)
        except Category.DoesNotExist:
            return JsonResponse({"error": "Category not found"}, status=404)
    elif request.method =='GET':
        try:
            category = Category.objects.get(id=category_id)
            ideas = Idea.objects.filter(category=category)
            json_response = [
                {
                    "id": idea.id,
                    "author_id": idea.user.id,
                    "idea_name": idea.title,
                    "description": idea.description
                }
                for idea in ideas
            ]
            return JsonResponse(json_response, safe=False, status=200)
        except Category.DoesNotExist:
            return JsonResponse({"error": "Category not found"}, status=404)

def __get_request_user(request):
    header_token = request.headers.get('Api-Session-Token', None)
    if header_token is None:
        return None
    try:
        db_session = UserSession.objects.get(token=header_token)
        return db_session.creator
    except UserSession.DoesNotExist:
        return None

@csrf_exempt
def comments(request, idea_id):
    if request.method == 'POST':
        # El usuario va a añadir un comentario a la idea
        try:
            idea = Idea.objects.get(id=idea_id)
            body_json = json.loads(request.body)
            json_content = body_json['content']  # El contenido del comentario

            # Obtener al usuario autenticado mediante el token
            authenticated_user = __get_request_user(request)
            if authenticated_user is None:
                return JsonResponse({"error": "Not valid or missing token"}, status=401)

            # Crear y guardar el nuevo comentario
            comment = Comment()
            comment.user = authenticated_user
            comment.content = json_content
            comment.idea = idea
            comment.save()

            return JsonResponse({"success": True}, status=201)

        except KeyError:
            return JsonResponse({"error": "Missing parameter in json request body"}, status=400)
        except Idea.DoesNotExist:
            return JsonResponse({"error": "Idea does not exist"}, status=404)
    elif request.method == 'GET':
        try:
            # Obtener la idea por su ID
            idea = Idea.objects.get(id=idea_id)

            # Recuperar todos los comentarios asociados a la idea
            comments_list = [
                {
                    "id": comment.id,
                    "author_id": comment.user.id,
                    "content": comment.content
                }
                for comment in Comment.objects.filter(idea=idea)
            ]

            return JsonResponse(comments_list, safe=False, status=200)

        except Idea.DoesNotExist:
            return JsonResponse({"error": f"Idea {idea_id} doesn't exist"}, status=404)

    else:
        return JsonResponse({'error': 'Unsupported HTTP method'}, status=405)

