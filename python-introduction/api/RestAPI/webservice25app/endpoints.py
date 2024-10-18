from django.http import JsonResponse

def my_first_endpoint(request):
    json_dictionary = {
        "ok": True,
        "message": "Todo correcto"
    }
    return JsonResponse(json_dictionary)
def my_not_found_endpoint(request):
    json_dictionary = {
        "message": "Lo siento, eso que buscas no anda por aquí"
    }
    return JsonResponse(json_dictionary, status=404)

