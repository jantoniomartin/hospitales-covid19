from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Profile


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'perfil'


class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline, )


#admin.site.unregister(User)
admin.site.register(User, UserAdmin)
