from django.shortcuts import render
from .models import Servicio

# Create your views here.
def servicios(request):
    datos_servicio = Servicio.objects.all()
    return render(request, "servicios/services.html", {'datos_servicio': datos_servicio})