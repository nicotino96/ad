import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Entry # Es necesario el punto (.)

@csrf_exempt
@csrf_exempt
def all_entries(request):
    if request.method == "GET":
        all_rows = Entry.objects.all()
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

