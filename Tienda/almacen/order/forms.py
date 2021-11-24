from django import forms
from django.db.models.base import Model
from django.forms import fields
from .models import Order

class estadoForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            'estado',
        )

        widgets = {
            'estado' : forms.Select(
                attrs={
                    'class':'form-control',
                }
            )
        }