from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactoForm

# Create your views here.
def contacto(request):
    #print("Tipo de petición: {}".format(request.metthod))
    formulario_contacto = ContactoForm()

    if request.method == "POST":
        formulario_contacto = ContactoForm(data=request.POST)
        if formulario_contacto.is_valid():
            nombre = request.POST.get('nombre','')
            correo_electronico = request.POST.get('correo_electronico','')
            contenido = request.POST.get('contenido','')

            email = EmailMessage(
                "La Caffettiera: Nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribió:\n\n{}".format(nombre, correo_electronico, contenido),
                "no-contestar@luisamos.com",
                ["luisamos7@gmail.com"],
                reply_to=[correo_electronico]
            )

            try:
                email.send()
                #Redireccionamos
                return redirect(reverse('contacto')+"?ok")
            except: return redirect(reverse('contacto')+"?fail")

    return render(request, "contact/contact.html", {'formulario': formulario_contacto})