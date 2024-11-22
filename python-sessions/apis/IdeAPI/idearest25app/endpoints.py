import json

import bcrypt
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

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


