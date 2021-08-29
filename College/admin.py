from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.

from django.contrib.auth.admin import UserAdmin

from .forms import PDEUCreationForm, PDEUChangeForm
from .models import PDEU


class PDEUAdmin(UserAdmin):
    add_form = PDEUCreationForm
    form = PDEUChangeForm
    model = PDEU
    list_display = ('email', 'is_staff', 'is_active','is_superuser','is_PDEU',)
    list_filter = ('email', 'is_staff', 'is_active','is_superuser','is_PDEU',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active','is_superuser','is_PDEU'),}),
        ('Group Permissions', {
            'classes': ('collapse',),
            'fields': ('groups', 'user_permissions', )
        })
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active','is_superuser','is_PDEU')}
        ),('Group Permissions', {
            'classes': ('collapse',),
            'fields': ('groups', 'user_permissions', )
        })
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(PDEU, PDEUAdmin)
