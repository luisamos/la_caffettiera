from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    fecha_modificacion = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ['-fecha_creacion']

    def __str__(self):
        return self.nombre

class Post(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Nombre")
    contenido = models.TextField(verbose_name="Contenido")
    fecha_publicacion = models.DateTimeField(verbose_name="Fecha de publicación", default=now)
    imagen = models.ImageField(verbose_name="Imagen", upload_to="blog", null=True, blank=True) 
    #autor = models.ForeignKey(User, verbose_name="Autor", on_delete=models.PROTECT, null=True, blank=True)
    autor = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)
    categoria = models.ManyToManyField(Categoria, verbose_name="Categorias", related_name="get_posts")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    fecha_modificacion = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")

    class Meta:
        verbose_name = "Entrada"
        verbose_name_plural = "Entradas"
        ordering = ['-fecha_creacion']

    def __str__(self):
        return self.titulo
