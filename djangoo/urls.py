from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls), # Acceso al panel de control [cite: 184]
    path('bands/', include('bands.urls')), # Todo lo de música vivirá aquí [cite: 572, 574]
    path('', include('main.urls')), # Tu código anterior sigue funcionando igual
]