from django.db import models

class Producto(models.Model):
    categoria = models.CharField(max_length=32)
    marca = models.CharField(max_length=15)
    modelo = models.CharField(max_length=20)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to='Img', null=True)

    def __str__(self):
        return f'{self.categoria} -> {self.precio}'