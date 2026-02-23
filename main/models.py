from django.db import models

class Post(models.Model):
    """
    Model representing a blog post or announcement on the home page.
    """
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
