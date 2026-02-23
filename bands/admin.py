from django.contrib import admin
from .models import Musician, Band, Venue, Room

# Registro básico
admin.site.register(Musician)
admin.site.register(Band)
admin.site.register(Venue)
admin.site.register(Room)