from django.contrib import admin
from .models import Enlace

# Register your models here.
class EnlaceAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_creacion', 'fecha_modificacion')

    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name="Personal").exists():
            return ('clave', 'nombre', 'fecha_creacion', 'fecha_modificacion')
        else:
            return ('fecha_creacion', 'fecha_modificacion')

admin.site.register(Enlace, EnlaceAdmin)