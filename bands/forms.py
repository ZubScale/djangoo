from django import forms
from .models import Musician

class MusicianForm(forms.ModelForm):
    """
    Form for creating and updating Musician instances.
    """
    class Meta:
        model = Musician
        fields = ['first_name', 'last_name', 'birth']
        # Esto añade el calendario de Windows al campo de fecha
        widgets = {
            'birth': forms.DateInput(attrs={'type': 'date'}),
        }
