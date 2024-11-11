import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Dashboard, Answer
from .models import Question

def all_dashboards(request):
    if request.method != "GET":
        return JsonResponse({"error": "HTTP method not supported"}, status=405)
    all_rows = Dashboard.objects.all()
    json_response = []
    for row in all_rows:
        json_response.append(row.to_json())
    return JsonResponse(json_response, safe=False)
@csrf_exempt
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
    elif request.method == "POST":
        client_json = json.loads(request.body)
        client_title = client_json.get("title", None)
        client_summary = client_json.get("summary", None)
        if client_title is None or client_summary is None:
            return JsonResponse({"error": "Missing summary or title in request body"}, status=400)
        new_question = Question(title=client_title, summary=client_summary, dashboard_id=path_param_id)
        new_question.save()
        return JsonResponse({"success": True}, status=201)

    else:
        return JsonResponse({"error": "HTTP method not supported"}, status=405)
@csrf_exempt
def answers_for_questions(request, question_id):
    if request.method == "GET":
        answers = Answer.objects.filter(question_id=question_id).order_by('-publication_date')
        if answers is not None:
            json_response = []
            for row in answers:
                json_response.append(row.to_json())
            return JsonResponse(json_response, safe=False)
        else:
            return JsonResponse({"error": "Not found"}, status=405)
    elif request.method == "POST":
        client_json = json.loads(request.body)
        client_summary = client_json.get("summary", None)
        if client_summary is None:
            return JsonResponse({"error": "Missing summary or title in request body"}, status=400)
        try:
            question = Question.objects.get(id=question_id)
        except Question.DoesNotExist:
            return JsonResponse({"error": "No question"}, status=404)
        new_answer = Answer(question=question, description=client_summary)
        new_answer.save()
        return JsonResponse({"success": True}, status=201)

    else:
        return JsonResponse({"error": "HTTP method not supported"}, status=405)

