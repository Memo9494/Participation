from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    matricula = models.CharField(max_length=10, null=True, blank=True)
    carrera = models.CharField(max_length=50, null=True, blank=True)
    semestre = models.CharField(max_length=10, null=True, blank=True)
    nombre = models.CharField(max_length=50, null=True, blank=True)
    apellido = models.CharField(max_length=50, null=True, blank=True)
    
    
