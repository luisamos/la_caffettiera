from django.contrib import admin
from .models import Categoria, Post

# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_creacion', 'fecha_modificacion')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_creacion', 'fecha_modificacion')
    list_display = ('titulo', 'autor' , 'nombre_categoria', 'fecha_publicacion')
    ordering = ('autor', 'fecha_publicacion')
    #Si quieres un orde de una sola dupla
    #ordering = ('autor',)
    search_fields = ('titulo', 'contenido', 'autor__username', 'categoria__nombre',)
    date_hierarchy = 'fecha_publicacion'
    list_filter = ('autor__username', 'categoria__nombre')

    def nombre_categoria(self, obj):
        return ", ".join([c.nombre for c in obj.categoria.all().order_by("nombre")])

    nombre_categoria.short_description = "Categorías"
    


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Post, PostAdmin)