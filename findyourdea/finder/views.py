from django import http
from django.shortcuts import render
from django.http import HttpResponse
from .models import Dea
from .queries import *
#FORM_TEST:
def user(request):
    print(request)
    return render(request, "finder/user.html")

def index(request):
    if request.method == "POST":
        lat = float(request.POST["lat"])
        long = float(request.POST["long"])

        print(lat, long)
        result, dea_latlng = get_nearest_dea(lat,long, Dea.objects.all()) # 40.4237241,-3.6748421
        context = {"dea": result, "anchor_tag": f"https://www.google.com/maps/search/?api=1&query={dea_latlng[0]},{dea_latlng[1]}"}
        return render(request, "finder/index.html", context)
    else:
        context = {"dea": {"direccion_ubicacion": "Indica tu posición"}, "anchor_tag": "#"}
        return render(request, "finder/index.html", context)


def todoslosdeas(request):
    return render(request, "finder/todoslosdeas.html")

def comments(request):
    return HttpResponse("Esta en la sección de comentarios")