from django import http
from django.shortcuts import render
from django.http import HttpResponse
from .models import Dea
from .queries import *

def index(request):
    result, dea_latlng = get_nearest_dea(40.4240319, -3.6724659, Dea.objects.all())
    context = {"dea": result, "anchor_tag": f"https://www.google.com/maps/search/?api=1&query={dea_latlng[0]},{dea_latlng[1]}"}
    return render(request, "finder/index.html", context)

def todoslosdeas(request):
    return render(request, "finder/todoslosdeas.html")

def comments(request):
    return HttpResponse("Esta en la sección de comentarios")