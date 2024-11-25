import json

import bcrypt
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import secrets
from .models import UserSession, Category, Idea
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
            idea.title = json_title
            idea.description = json_description
            idea.category = category
            idea.save()
            return JsonResponse({"success": True}, status=201)
        except KeyError:
            return JsonResponse({"error": "You are missing a parameter"}, status=400)
        except Category.DoesNotExist:
            return JsonResponse({"error": "Category not found"}, status=404)
    elif request.method == 'GET':
    # El usuario quiere consultar las ideas de la categoría con id == category_id
    pass
    else:
    return JsonResponse({'error': 'HTTP method unsupported'}, status=405)



