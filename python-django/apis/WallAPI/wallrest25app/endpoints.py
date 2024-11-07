from django.http import JsonResponse
from .models import Entry # Es necesario el punto (.)

def all_entries(request):
    if request.method != "GET":
        return JsonResponse({"error": "HTTP method not supported"}, status=405)
    all_rows = Entry.objects.all()
    json_response = [] # Esta variable sirve como acumulador
    for row in all_rows:
        # Iteramos sobre cada fila SQL de la tabla Entry
        json_response.append(row.to_json())
    return JsonResponse(json_response, safe=False)

