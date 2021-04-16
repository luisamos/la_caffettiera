from django.db import models

# Create your models here.
class Enlace(models.Model):
    clave = models.SlugField(verbose_name="Nombre clave", max_length=100,unique=True)
    nombre = models.CharField(verbose_name="Red social", max_length=200)
    enlace_web = models.URLField(verbose_name="Enlace web", max_length=200, null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    fecha_modificacion = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")

    class Meta:
        verbose_name = "Enlace"
        verbose_name_plural = "Enlaces"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre
