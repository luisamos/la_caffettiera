from django.db import models
from ckeditor.fields import RichTextField 

# Create your models here.
class Pagina(models.Model):
    
    titulo = models.CharField(verbose_name="Título", max_length=200)
    #contenido = models.TextField(verbose_name="Contenido")
    contenido = RichTextField(verbose_name="Contenido")
    orden = models.SmallIntegerField(verbose_name="Orden", default=0)
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    fecha_modificacion = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")

    class Meta:
        verbose_name = "Página"
        verbose_name_plural = "Páginas"
        ordering = ['-orden',]

    def __str__(self):
        return self.titulo