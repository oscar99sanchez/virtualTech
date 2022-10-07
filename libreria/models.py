from tabnanny import verbose
from unicodedata import category
from django.db import models

# Create your models here.
class Mouses(models.Model):
    id = models.AutoField(primary_key=True)

    MOUSES = 'MS'
    TECLADOS = 'TC'
    MONITORES = 'MN'
    MOUSE_PAD = 'MP'
    DIADEMAS = 'DD'

    LISTA_CATEGORIAS = [
        ('MS', 'Mouses'),
        ('TC', 'Teclados'),
        ('MN', 'Monitores'),
        ('MP', 'Mouse pad'),
        ('DD', 'Diademas'),
    ]
    categorias = models.CharField(
        max_length=2,
        choices=LISTA_CATEGORIAS,
        default=MOUSES,
    )

    producto = models.TextField(max_length=10, verbose_name='Productoo', null=True)
    img = models.TextField(max_length=1000, verbose_name='link de la image', null=True)
    precio = models.IntegerField(verbose_name='Precio', null=True)

    def __str__(self):
        fila = self.categorias
        return  fila

