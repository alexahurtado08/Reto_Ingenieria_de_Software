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

    
    OfertaLaboral = models.ForeignKey('OfertaLaboral', on_delete=models.SET_NULL, null=True, blank=True)
    nombre = models.CharField(max_length=200)
    contenido = models.TextField()
    plataformas = models.ManyToManyField(Plataforma)
    presupuesto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_inicio = models.DateTimeField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='activa')
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
    
    
class Postulacion(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    medio_conocimiento = models.CharField(max_length=50)
    edad = models.PositiveIntegerField()
    genero = models.CharField(max_length=20)
    pais = models.CharField(max_length=50)
    departamento = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    nivel_estudios = models.CharField(max_length=50)
    fecha_postulacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre