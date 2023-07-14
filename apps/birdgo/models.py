from django.db import models

# Create your models here.

class Bird(models.Model):
    id_ave = models.IntegerField(primary_key=True)
    nombre_ave = models.CharField(max_length=20, null=False)
    nombre_cientifico = models.CharField(max_length=30, null=True)
    imagen_ave = models.ImageField(upload_to='imagenesAves',null=False)