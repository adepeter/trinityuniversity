from django.contrib import admin


# Register your models here.
from ..models import Programme


@admin.register(Programme)
class ProgrammeAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'slug',
        'start_date'
    ]
    prepopulated_fields = {
        'slug': ('name',)
    }
