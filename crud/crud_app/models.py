from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre_completo = models.CharField(max_length=100)
    peso = models.CharField(max_length=10)
    talla = models.CharField(max_length=10)
    
    def __str__(self) -> str:
        return self.nombre_completo