from django.contrib import admin

# Register your models here.
from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'slug',
        'date_posted',
        'date_modified',
    ]
    prepopulated_fields = {
        'slug': ('name',)
    }
    date_hierarchy = 'date_posted'
