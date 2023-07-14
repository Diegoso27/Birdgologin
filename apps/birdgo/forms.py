from django import forms
from django.forms import ModelForm
from .models import *

class BirdsForm(ModelForm):
    class Meta:
        model = Bird
        fields = [
          'id_ave',
          'nombre_ave',
          'nombre_cientifico',
          'imagen_ave'
        ]

        labels = {
          'id_ave' : 'ID Ave',
          'nombre_ave' : 'Nombre Ave',
          'nombre_cientifico' : 'Nombre cientÃ­fico',
          'imagen_ave' : 'Imagen'
        }

        widgets = {
          'id_ave':forms.TextInput(attrs={'class':'form-control'}),
          'nombre_ave':forms.TextInput(attrs={'class':'form-control'}),
          'nombre_cientifico':forms.TextInput(attrs={'class':'form-control'}),
          'imagen_ave':forms.FileInput(attrs={'class': 'form-control'})
        }