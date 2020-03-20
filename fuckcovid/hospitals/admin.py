from django.contrib import admin
from fuckcovid.hospitals.models import Region, Hospital, Resource, Need


class NeedInline(admin.TabularInline):
    model = Need


class HospitalAdmin(admin.ModelAdmin):
    inlines = [
        NeedInline,
    ]


class ResourceAdmin(admin.ModelAdmin):
    inlines = [
        NeedInline,
    ]

admin.site.register(Region)
admin.site.register(Hospital, HospitalAdmin)
admin.site.register(Resource, ResourceAdmin)

