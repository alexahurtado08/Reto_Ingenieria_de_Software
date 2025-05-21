from django import forms
from .models import OfertaLaboral, Campania

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

class CampaniaForm(forms.ModelForm):
    class Meta:
        model = Campania
        fields = ['nombre', 'contenido', 'presupuesto', 'fecha_inicio', 'plataformas', 'OfertaLaboral']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-input'}),
            'contenido': forms.Textarea(attrs={'class': 'form-textarea'}),
            'presupuesto': forms.NumberInput(attrs={'class': 'form-input'}),
            'fecha_inicio': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-input'}),
            'plataformas': forms.CheckboxSelectMultiple(),
            'OfertaLaboral': forms.Select(attrs={'class': 'form-input'}),
        }
