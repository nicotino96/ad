from django.http import JsonResponse


def wishlist(request):
    response_data = {
        "mensaje": "Por aprobar Acceso a Datos quiero",
        "deseos": [
            "PlayStation 8",
            "Ordenador i9 con gráfica potente",
            "Yoyó"
        ]
    }
    return JsonResponse(response_data)