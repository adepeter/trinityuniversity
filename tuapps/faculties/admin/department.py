from django.contrib import admin


# Register your models here.
from ..models import Department


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'faculty'
    ]
    prepopulated_fields = {
        'slug': ('name',)
    }
    list_filter = [
        'faculty'
    ]
