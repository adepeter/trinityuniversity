from django.contrib import admin
from django.db import models

# Register your models here.
from martor.widgets import AdminMartorWidget

from ..models import Faculty, FacultyMembership


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'dean'
    ]
    prepopulated_fields = {
        'slug': ('name',)
    }
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }


@admin.register(FacultyMembership)
class FacultyMembershipAdmin(admin.ModelAdmin):
    list_display = [
        'staff',
        'faculty',
        'date_joined'
    ]
