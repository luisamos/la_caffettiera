from django import template
from pages.models import Pagina

register = template.Library()

@register.simple_tag
def get_lista_pagina():
    datos_pagina = Pagina.objects.all()
    return datos_pagina
