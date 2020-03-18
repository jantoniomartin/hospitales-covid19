from django.db import models


class Region(models.Model):
    name = models.CharField("nombre", max_length=50, unique=True)

    class Meta:
        verbose_name = "Región"
        verbose_name_plural = "Regiones"

    def __str__(self):
        return self.name

class Hospital(models.Model):
    phone = models.CharField("teléfono", max_length=15)
    name = models.CharField("nombre", max_length=100)
    address = models.CharField("dirección", max_length=255)
    region = models.ForeignKey('Region', verbose_name="región", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Hospital"
        verbose_name_plural = "Hospitales"

    def __str__(self):
        return f"{self.name} ({self.region})"
