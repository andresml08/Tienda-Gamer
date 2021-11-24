from django import forms
from django.db.models.base import Model
from django.forms import fields
from .models import Producto

class ProdForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = (
            'categoria',
            'marca',
            'modelo',
            'precio',
            'imagen',
        )

        widgets = {
             'categoria' : forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Categoria',
                     'style':'margin-top:1rem',
                }
            ),
             
              'marca' : forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Marca',
                    'style':'margin-top:1rem',
                    
                }
            ),
              
             'modelo' : forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Modelo',
                    'style':'margin-top:1rem',
                }
            ),
             
             
             'precio' : forms.NumberInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Precio',
                    'style':'margin-top:1rem',
                }
            ),
             
      
        }