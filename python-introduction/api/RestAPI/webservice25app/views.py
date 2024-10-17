from django.shortcuts import render
from django.http import HttpResponse

def my_first_view(request):
    return HttpResponse("Hola a todo el mundo, ahora bien hecho")

