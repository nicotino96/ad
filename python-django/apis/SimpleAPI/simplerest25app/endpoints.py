from django.http import JsonResponse

def health_check(request):
    http_response = {"running": True}
    return JsonResponse(http_response)
