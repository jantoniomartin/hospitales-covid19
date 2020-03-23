from django.db import models
from django.conf import settings
from django.db.models import Sum
from django.urls import reverse


class Region(models.Model):
    name = models.CharField("nombre", max_length=50, unique=True)

    class Meta:
        verbose_name = "Región"
        verbose_name_plural = "Regiones"

    def __str__(self):
        return self.name


class Hospital(models.Model):
    city = models.CharField("localidad", max_length=100, blank=True, null=True)
    phone = models.CharField("teléfono", max_length=15)
    name = models.CharField("nombre", max_length=100)
    address = models.CharField("dirección", max_length=255)
    region = models.ForeignKey('Region', verbose_name="región", on_delete=models.CASCADE)
    comment = models.TextField("comentario", blank=True, null=True)

    class Meta:
        verbose_name = "Hospital"
        verbose_name_plural = "Hospitales"
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('hospitals:hospital-detail', args=[str(self.id)])


class Resource(models.Model):
    name = models.CharField("nombre", max_length=255, unique=True)

    class Meta:
        verbose_name = "Recurso"
        verbose_name_plural = "Recursos"
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_total_needs(self):
        total = self.need_set.aggregate(total_per_day=Sum('amount_per_day'))['total_per_day']
        if total is not None:
            return total
        return 0

    def get_total_production(self):
        total = self.production_set.aggregate(total_per_day=Sum('amount_per_day'))['total_per_day']
        if total is not None:
            return total
        return 0

    def get_deficit(self):
        deficit = self.get_total_needs() - self.get_total_production()
        return deficit if deficit >= 0 else 0

    @property
    def weekly_commitment(self):
        return Commitment.objects.filter(
            need__resource=self).aggregate(
                Sum('amount_per_week'))['amount_per_week__sum']

    @property
    def daily_commitment(self):
        weekly = self.weekly_commitment
        return int(weekly / 7) if weekly else None


class Need(models.Model):
    hospital = models.ForeignKey('Hospital', verbose_name="hospital", on_delete=models.CASCADE)
    resource = models.ForeignKey('Resource', verbose_name="recurso", on_delete=models.CASCADE)
    amount_per_day = models.PositiveIntegerField('cantidad por día', default=0)
    comment = models.TextField("comentario", blank=True, null=True)
    editor = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="editor", on_delete=models.CASCADE)
    created_at = models.DateTimeField("alta", auto_now_add=True)
    updated_at = models.DateTimeField("actualizado", auto_now=True)

    class Meta:
        verbose_name = "Necesidad"
        verbose_name_plural = "Necesidades"

    def __str__(self):
        return str(self.resource)

class Commitment(models.Model):
    need = models.ForeignKey(Need, on_delete=models.CASCADE)
    maker = models.ForeignKey('makers.Maker', on_delete=models.CASCADE)
    amount_per_week = models.PositiveIntegerField('Cantidad por semana',
        default=0)
    