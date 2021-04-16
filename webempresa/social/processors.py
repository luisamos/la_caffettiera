from .models import Enlace

def diccionario_contexto(request):
    contexto = {}
    datos_enlace = Enlace.objects.all()
    for i in datos_enlace:
        contexto[i.clave] = i.enlace_web
    return contexto