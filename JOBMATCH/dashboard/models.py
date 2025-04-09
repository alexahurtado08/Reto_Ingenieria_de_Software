from django.db import models
from django.contrib.auth.models import User

class Plataforma(models.Model):
    nombre = models.CharField(max_length=50)
    api_key = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.nombre

class Campania(models.Model):
    ESTADOS = (
        ('activa', 'Activa'),
        ('pausada', 'Pausada'),
        ('finalizada', 'Finalizada'),
    )

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    OfertaLaboral = models.ForeignKey('OfertaLaboral', on_delete=models.SET_NULL, null=True, blank=True)
    nombre = models.CharField(max_length=200)
    contenido = models.TextField()
    plataformas = models.ManyToManyField(Plataforma)
    presupuesto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_inicio = models.DateTimeField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pausada')
    id_facebook = models.CharField(max_length=100, blank=True)  # ID de la campaña en Meta

    def __str__(self):
        return self.nombre

class Multimedia(models.Model):
    campania = models.ForeignKey(Campania, on_delete=models.CASCADE, related_name='archivos')
    archivo = models.FileField(upload_to='campañas/')
    tipo = models.CharField(max_length=50)  # imagen/video
    subido_en = models.DateTimeField(auto_now_add=True)
    
class OfertaLaboral(models.Model):
    cargo = models.CharField(max_length=100)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    ubicacion = models.CharField(max_length=100)
    critica = models.BooleanField(default=False)

    def __str__(self):
        return self.cargo