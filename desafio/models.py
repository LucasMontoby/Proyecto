from django.db import models

# Create your models here.

class Familiar1(models.Model):
    nombre = models.CharField(max_length=30)
    phone = models.IntegerField(verbose_name='Telefono')
    fecha_nacimiento = models.DateField(null=True)
    
class Familiar2(models.Model):
    nombre = models.CharField(max_length=30)
    phone = models.IntegerField(verbose_name='Telefono')
    fecha_nacimiento = models.DateField(null=True)
    
class Familiar3(models.Model):
    nombre = models.CharField(max_length=30)
    phone = models.IntegerField(verbose_name='Telefono')
    fecha_nacimiento = models.DateField(null=True)
    
    