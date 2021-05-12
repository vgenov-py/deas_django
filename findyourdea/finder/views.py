from django import http
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "finder/index.html")

def comments(request):
    return HttpResponse("Esta en la sección de comentarios")