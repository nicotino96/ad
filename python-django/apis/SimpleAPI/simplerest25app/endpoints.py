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
