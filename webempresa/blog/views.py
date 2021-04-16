from django.shortcuts import render, get_object_or_404
from .models import Post, Categoria

# Create your views here.
def blog(request):
    datos_post = Post.objects.all()
    return render(request, "blog/blog.html", {'datos_post': datos_post})

def categoria(request, categoria_id):
    datos_categoria = get_object_or_404(Categoria, id=categoria_id)
    return render(request, "blog/category.html", {'datos_categoria': datos_categoria})