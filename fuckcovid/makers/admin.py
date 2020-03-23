from django.contrib import admin
from ..hospitals.models import Commitment
from .models import Maker, Production


class ProductionInline(admin.TabularInline):
    model = Production

class CommitmentInline(admin.TabularInline):
    model = Commitment

class MakerAdmin(admin.ModelAdmin):
    inlines = [
        ProductionInline,
        CommitmentInline,
    ]


admin.site.register(Maker, MakerAdmin)
