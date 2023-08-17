from django.db import models
from django.contrib.auth.models import User

class Instrumento(models.Model):
    tipo = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    precio = models.FloatField(null=False, blank=False)

    def __str__(self):
        return f"{self.tipo} {self.marca} - {self.modelo}"
    
class Disco(models.Model):
    artista = models.CharField(max_length=50)
    album = models.CharField(max_length=50)
    precio = models.FloatField()

    def __str__(self):
        return f"{self.album} - {self.artista}"

class Remera(models.Model):
    modelo = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    precio = models.FloatField()

    def __str__(self):
        return f"Remera {self.modelo}, color {self.color}"
    
class Ticket(models.Model):
    artista = models.CharField(max_length=50)
    fecha = models.DateField()
    precio = models.FloatField()

    def __str__(self):
        return f"Ticket para {self.artista} el {self.fecha}"
 
class UserAvatar(models.Model):
    image = models.ImageField(upload_to="avatars")
    user = models.ForeignKey(User, on_delete= models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.image}"