from django.contrib import admin


# Register your models here.
from ..models import Level


@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = [
        'name'
    ]
