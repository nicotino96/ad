from django.http import JsonResponse

def my_first_endpoint(request):
    json_dictionary = {
        "ok": True,
        "message": "Todo correcto"
    }
    return JsonResponse(json_dictionary)

