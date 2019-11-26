from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    quantidade = models.IntegerField()
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    descricao= models.TextField()
    photo = models.ImageField(upload_to='clients_photos', null='true', blank='true')

    def __str__(self):
        return self.name + ' - ' + self.type