from django.http import JsonResponse

def health_check(request):
    http_response = {"running": True}
    return JsonResponse(http_response)


def table_of_six(request):
    http_response = [6 * i for i in range(1, 11)]

    return JsonResponse(http_response, safe=False)
