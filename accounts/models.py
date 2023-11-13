from django.db import models
from django.contrib.auth.models import AbstractUser
from cryptography.fernet import Fernet

#utilizar la llave secreta para encriptar nombres de los usuarios
secret_key = b'HCSP-XM-YJ7L4Z_1HN7_Y86v75l0UZpejRBSq_CAv8A='
cipher_suite = Fernet(secret_key)

# Create your models here.
class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    matricula = models.CharField(max_length=10, null=True, blank=True)
    carrera = models.CharField(max_length=50, null=True, blank=True)
    semestre = models.CharField(max_length=10, null=True, blank=True)
    nombre = models.CharField(max_length=100, null=True, blank=True)
    apellido = models.CharField(max_length=100, null=True, blank=True)

    
    def encrypt_nombre(self, nombre):
        if nombre:
            encrypted_nombre = cipher_suite.encrypt(nombre.encode())
            #use only the string data
            encrypted_nombre = encrypted_nombre.decode()
            print(encrypted_nombre)
            return encrypted_nombre
        return None

    def save(self, *args, **kwargs):
        if self.nombre:
            self.nombre = self.encrypt_nombre(self.nombre)
        if self.apellido:
            self.apellido = self.encrypt_nombre(self.apellido)
            
        super().save(*args, **kwargs)

    def decrypt_nombre(self, encrypted_nombre):
        if encrypted_nombre:
            decrypted_nombre = cipher_suite.decrypt(encrypted_nombre).decode()
            return decrypted_nombre
        return None

    def get_nombre(self):
        return self.decrypt_nombre(self.nombre)
    
