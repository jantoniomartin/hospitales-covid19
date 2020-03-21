from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField("nombre", max_length=255)
    surname = models.CharField("apellidos", max_length=255)
    company = models.CharField("empresa", max_length=255, blank=True, null=True)
    address = models.TextField("dirección", blank=True, null=True)
    phone = models.CharField("teléfono", max_length=15, blank=True, null=True)
    city = models.CharField("localidad", max_length=100, blank=True, null=True)
    country = models.CharField("localidad", max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = "perfil"
        verbose_name_plural = "perfiles"
