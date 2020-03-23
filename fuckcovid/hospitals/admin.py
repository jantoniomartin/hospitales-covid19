from django.contrib import admin
from fuckcovid.hospitals.models import Region, Hospital, Resource, Need


class NeedInline(admin.TabularInline):
    model = Need


class NeedInline(admin.TabularInline):
    model = Need


class HospitalAdmin(admin.ModelAdmin):
    inlines = [
        NeedInline,
    ]


class ResourceAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'get_total_needs', 
        'daily_commitment',
    )
    inlines = [
        NeedInline,
    ]

admin.site.register(Region)
admin.site.register(Hospital, HospitalAdmin)
admin.site.register(Resource, ResourceAdmin)
