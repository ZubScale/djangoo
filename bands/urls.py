from django.urls import path
from bands import views

urlpatterns = [
    # List of all musicians
    path('musicians/', views.musicians, name="musicians"),

    # Detail view for a specific musician
    path('musician/<int:musician_id>/', views.musician, name="musician"),

    # Form to add a new musician
    path('add_musician/', views.musician_add, name="musician_add"),

    # List of all bands
    path('bands/', views.bands, name="bands"),

    # List of all venues
    path('venues/', views.venues, name="venues"),
]
