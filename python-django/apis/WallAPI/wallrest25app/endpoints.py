import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Entry, Comment  # Es necesario el punto (.)

@csrf_exempt
@csrf_exempt
def all_entries(request):
    if request.method == "GET":
        size = request.GET.get("size", None)
        if size is not None:
            try:
                size = int(size)
            except ValueError:
                return JsonResponse({"error": "Wrong size parameter"}, status=400)
        if size is None:
            all_rows = Entry.objects.order_by("-publication_date")
        else:
            all_rows = Entry.objects.order_by("-publication_date")[:size]
        json_response = []
        for row in all_rows:
            json_response.append(row.to_json())
        return JsonResponse(json_response, safe=False)
    elif request.method == "POST":
        client_json = json.loads(request.body)
        entry_title = client_json.get("new_title", None)
        entry_content = client_json.get("new_content", None)
        if entry_title is None or entry_content is None:
            return JsonResponse({"error": "Missing new_title or new_content"}, status=400)
        new_entry = Entry(title=entry_title, content=entry_content)
        new_entry.save()
        return JsonResponse({"it_was_ok": True}, status=201)
    else:
        return JsonResponse({"error": "HTTP method not supported"}, status=405)
@csrf_exempt
def entry_comments(request, path_param_id):
    if request.method == "GET":
        comments = Comment.objects.filter(entry=path_param_id)
        json_response = []
        for row in comments:
            json_response.append(row.to_json())
        return JsonResponse(json_response, safe=False)
    elif request.method == "POST":
        client_json = json.loads(request.body)
        client_content = client_json.get("new_content", None)
        if client_content is None:
            return JsonResponse({"error": "Missing new_content"}, status=400)
            # Creamos una nueva instancia de Comment
            # Nótese pasamos entry_id=... en vez de entry=...
            # para indicar que nos referimos a la clave primaria (id)
            # del atributo. Esto se hace así para los models.ForeignKey
        new_comment = Comment(content=client_content, entry_id=path_param_id)
        new_comment.save()
        return JsonResponse({"new_comment_created": True}, status=201)
    else:
        return JsonResponse({"error": "HTTP method not supported"}, status=405)



