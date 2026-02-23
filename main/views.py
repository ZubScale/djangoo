from django.shortcuts import render
from .models import Post

def home(request):
    """
    Vista para la página de inicio.

    Args:
        request: HttpRequest object.

    Returns:
        HttpResponse: Rendered home page with list of posts.
    """
    posts = Post.objects.all()
    return render(request, 'home.html', {
        'posts': posts
    })
