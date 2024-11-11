from django.http import JsonResponse
from .models import Dashboard
from .models import Question

def all_dashboards(request):
    if request.method != "GET":
        return JsonResponse({"error": "HTTP method not supported"}, status=405)
    all_rows = Dashboard.objects.all()
    json_response = []
    for row in all_rows:
        json_response.append(row.to_json())
    return JsonResponse(json_response, safe=False)

def questions_from_dashboard(request, path_param_id):
    if request.method == "GET":
        before = request.GET.get("before", None)
        size = request.GET.get("size", None)

        if size is None:
            if before is None:
               questions = Question.objects.filter(dashboard=path_param_id).order_by('-publication_date')
            else:
                questions = Question.objects.filter(dashboard=path_param_id).filter(publication_date__lt=before).order_by("-publication_date")
        else:
            try:
                size = int(size)
            except ValueError:
                return JsonResponse({"error": "Wrong size parameter"}, status=400)
            if before is None:
                questions = Question.objects.filter(dashboard=path_param_id).order_by('-publication_date')[:size]
            else:
                questions = Question.objects.filter(dashboard=path_param_id).filter(publication_date__lt=before).order_by("-publication_date")[:size]

        json_response = []
        for row in questions:
            json_response.append(row.to_json())
        return JsonResponse(json_response, safe=False)
    else:
        return JsonResponse({"error": "HTTP method not supported"}, status=405)

