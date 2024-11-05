import json
from datetime import datetime
from random import sample
from django.views.decorators.csrf import csrf_exempt

from django.db.models.expressions import result
from django.http import JsonResponse

def health_check(request):
    http_response = {"running": True}
    return JsonResponse(http_response)


def table_of_six(request):
    http_response = [6 * i for i in range(1, 11)]

    return JsonResponse(http_response, safe=False)

def multiplication_table(request, number):
    if number == "one":
        return JsonResponse([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], safe=False)
    elif number == "two":
        return JsonResponse([2, 4, 6, 8, 10, 12, 14, 16, 18, 20], safe=False)
    elif number == "three":
        return JsonResponse([3, 6, 9, 12, 15, 18, 21, 24, 27, 30], safe=False)
    elif number == "four":
        return JsonResponse([4, 8, 12, 16, 20, 24, 28, 32, 36, 40], safe=False)
    elif number == "five":
        return JsonResponse([5, 10, 15, 20, 25, 30, 35, 40, 45, 50], safe=False)
    elif number == "six":
        return JsonResponse([6, 12, 18, 24, 30, 36, 42, 48, 54, 60], safe=False)
    elif number == "seven":
        return JsonResponse([7, 14, 21, 28, 35, 42, 49, 56, 63, 70], safe=False)
    elif number == "eight":
        return JsonResponse([8, 16, 24, 32, 40, 48, 56, 64, 72, 80], safe=False)
    elif number == "nine":
        return JsonResponse([9, 18, 27, 36, 45, 54, 63, 72, 81, 90], safe=False)
    elif number == "ten":
        return JsonResponse([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], safe=False)
    else:
        return JsonResponse({"error": "Number not valid. Only one to ten are supported"}, status=404)
def multiply_number_improved(request, number):
    result = []
    for i in range(1, 11):
        result.append(number * i)
    return JsonResponse(result,safe=False)
def multiplication_table_query_param(request):
    number = request.GET.get("i", None)
    if number is not None:
        try:
            number = int(number)
        except ValueError:
            return JsonResponse({"error": "Parameter 'i' must be a number"}, status=400)
        result = []

        for i in range(1, 11):
            result.append(number * i)
        return JsonResponse(result, safe=False)
    else:
        return JsonResponse({"error": "Missing 'i' parameter"}, status=400)
def number_is_prime(request):
    number = request.GET.get("q",None)
    if number is not None:
        try:
            number = int(number)
        except ValueError:
            return JsonResponse({"error": "Parameter must be a number bigger than zero"}, status=400)
        if number<1:
            return JsonResponse({"error": "Parameter must be a number bigger than zero"}, status=400)

        for i in range(2, number):
            if number%i==0:
                return JsonResponse({"is_prime_number": False})
        return JsonResponse({"is_prime_number": True})
    else:
        return JsonResponse({"error": "Missing required 'q' parameter"}, status=400)

def years_since(request, year):
    if year>datetime.now().year:
        return JsonResponse({"error": "Years in the future are invalid"}, status=400)
    else:
        return JsonResponse({"number_of_years": datetime.now().year-year})

@csrf_exempt
def resource_example(request, number):
    if request.method != 'POST':
        return JsonResponse({"error": "HTTP method not supported"}, status=405)
    # Precondición comprobada: El método es POST
    if len(request.body) == 0:
        # No hay cuerpo de petición
        # Nos comportamos como antes
        return JsonResponse({"message": "You have sent a POST to the resource " + str(number)})
    http_body = json.loads(request.body)
    client_mood = http_body.get("mood", "No mood")  # "No mood" será un valor por defecto
    return JsonResponse(
        {"message": "You have sent a POST to the resource " + str(number) + " and you're " + client_mood})
@csrf_exempt
def favorite_animal(request):
    if request.method != 'POST':
        return JsonResponse({"error": "HTTP method not supported"}, status=405)
    if len(request.body) == 0:
        return JsonResponse({"error": "no request body"}, status=400)
    http_body = json.loads(request.body)
    animal=http_body.get("name",None)
    if animal is None:
        return JsonResponse({"error": "No animal"}, status=400)
    elif animal=="Cat":
        return JsonResponse({"message": "Nice! Seven lives will be enough"})
    else:
        return JsonResponse({"message": "OK! Have a nice day"})









