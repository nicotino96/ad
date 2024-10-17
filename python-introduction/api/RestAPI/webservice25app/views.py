from django.shortcuts import render
from django.http import HttpResponse
from webservice25app import views

def my_first_view(request):
    return HttpResponse("Hola a todo el mundo, ahora bien hecho")
def vista_emperadores(request):
    return HttpResponse(
"""
    <html>
        <body>
            <h1>1, 2, probando...</h1>
            <p>A continuación se muestran tres emperadores romanos</p>
            <ul>
              <li>Augusto</li>
              <li>Claudio</li>
              <li>Nerón</li>
            </ul>
        </body>
    </html>
""")

