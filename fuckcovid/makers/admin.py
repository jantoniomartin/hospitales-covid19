from django.contrib import admin
from fuckcovid.makers.models import Maker, Production


class ProductionInline(admin.TabularInline):
    model = Production


class MakerAdmin(admin.ModelAdmin):
    inlines = [
        ProductionInline,
    ]


admin.site.register(Maker, MakerAdmin)
