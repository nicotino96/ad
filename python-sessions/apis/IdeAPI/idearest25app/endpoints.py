from django.http import JsonResponse

def health_check(request):
    http_response = {"is_living": True}
    return JsonResponse(http_response)