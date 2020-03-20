from django.db import models
from django.urls import reverse
from django.conf import settings
from fuckcovid.hospitals.models import Region, Resource


class Maker(models.Model):
    name = models.CharField("nombre", max_length=255, unique=True)
    city = models.CharField("localidad", max_length=100, blank=True, null=True)
    phone = models.CharField("teléfono", max_length=15)
    address = models.CharField("dirección", max_length=255)
    region = models.ForeignKey(Region, verbose_name="región", on_delete=models.CASCADE)
    comment = models.TextField("comentario", blank=True, null=True)
    editor = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="editor", on_delete=models.CASCADE)
    created_at = models.DateTimeField("alta", auto_now_add=True)
    updated_at = models.DateTimeField("actualizado", auto_now=True)

    class Meta:
        verbose_name = "maker"
        verbose_name_plural = "makers"
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('makers:maker-detail', args=[str(self.id)])


class Production(models.Model):
    maker = models.ForeignKey('Maker', verbose_name="maker", on_delete=models.CASCADE)
    resource = models.ForeignKey(Resource, verbose_name="recurso", on_delete=models.CASCADE)
    amount_per_day = models.PositiveIntegerField('capacidad por día', default=0)
    comment = models.TextField("comentario", blank=True, null=True)
    donation = models.BooleanField("donación", default=False)
    created_at = models.DateTimeField("alta", auto_now_add=True)
    updated_at = models.DateTimeField("actualizado", auto_now=True)

    class Meta:
        verbose_name = "producción"
        verbose_name_plural = "producciones"
        ordering = ['resource__name']

    def __str__(self):
        return f"{self.resource} ofrecido por {self.maker}"
