from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users import models


class CustomUserAdmin(UserAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

# Register your models here.
admin.site.register(models.User, CustomUserAdmin)
admin.site.register(models.FileData)
