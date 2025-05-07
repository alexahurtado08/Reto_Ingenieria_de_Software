from django import forms
from .models import OfertaLaboral
from .models import Campania

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
            'fecha_inicio': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'plataformas': forms.CheckboxSelectMultiple(),
        }

