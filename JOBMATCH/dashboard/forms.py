from django import forms
from .models import OfertaLaboral

class OfertaLaboralForm(forms.ModelForm):
    class Meta:
        model = OfertaLaboral
        fields = ['cargo', 'salario', 'ubicacion', 'critica']
        widgets = {
            'cargo': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Ej. Desarrollador Backend'}),
            'salario': forms.NumberInput(attrs={'class': 'form-input'}),
            'ubicacion': forms.TextInput(attrs={'class': 'form-input'}),
            'critica': forms.CheckboxInput(attrs={'class': 'form-checkbox'}),
        }
