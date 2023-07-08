from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.db import models

from arte import settings


class Artista_Model(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, default='no-email@example.com')
    phone = models.CharField(max_length=200, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name + ' ' + self.surname


class Obra_Model(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    artista = models.ForeignKey(Artista_Model, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + ' - ' + self.artista.name
