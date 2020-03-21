from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save


class User(AbstractUser):
    pass


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField("nombre", max_length=255, blank=True, null=True)
    surname = models.CharField("apellidos", max_length=255, blank=True, null=True)
    company = models.CharField("empresa", max_length=255, blank=True, null=True)
    address = models.TextField("dirección", blank=True, null=True)
    phone = models.CharField("teléfono", max_length=15, blank=True, null=True)
    city = models.CharField("localidad", max_length=100, blank=True, null=True)
    country = models.CharField("país", max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = "perfil"
        verbose_name_plural = "perfiles"


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

post_save.connect(create_profile, sender=User)
