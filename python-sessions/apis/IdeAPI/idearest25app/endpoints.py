import json

import bcrypt
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from idearest25app.models import CustomUser


def health_check(request):
    http_response = {"is_living": True}
    return JsonResponse(http_response)
@csrf_exempt
@csrf_exempt
def users(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Unsupported HTTP method'}, status=405)
    body_json = json.loads(request.body)
    json_username = body_json['username']
    json_email = body_json['useremail']
    json_password = body_json['password']
    # De momento no controlaremos peticiones de cliente erróneas. Sólo programamos el happy path
    salted_and_hashed_pass = bcrypt.hashpw(json_password.encode('utf8'), bcrypt.gensalt()).decode('utf8')
    user_object = CustomUser(e_mail=json_email, username=json_username, encrypted_password=salted_and_hashed_pass)
    user_object.save()
    return JsonResponse({"is_registered": True}, status=201) # Devolvemos al cliente un 201 Created

