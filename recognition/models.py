from django.db import models

class StoreFace(models.Model):

    created = models.DateField('Fecha', blank=False, null=False, auto_now_add=True)
    name = models.CharField('Nombre', max_length=120, blank=False, null=False)
    image = models.ImageField('Imagen', blank=False, null=False, upload_to='store_faces/')
    encoding = models.JSONField('Codificación Facial', blank=True, null=True)

    def __str__(self):
        return self.name