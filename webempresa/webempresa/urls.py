"""webempresa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#from core import views, urls
#from servicios import views, urls
from django.conf import settings

urlpatterns = [
    # Path del Core
    path('', include('core.urls')),
    # Path del Servicios
    path('servicios/', include('servicios.urls')),
    # Path del Blog
    path('blog/', include('blog.urls')),
    # Path de Página
    path('pagina/', include('pages.urls')),
    # Path Contacto
    path('contacto/', include('contact.urls')),
    # Path del administrador
    path('gestion/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)