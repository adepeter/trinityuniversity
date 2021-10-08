from django.contrib import admin


# Register your models here.
from ..models import HeadOfDepartment, Dean


@admin.register(Dean)
class DeanAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'faculty'
    ]


@admin.register(HeadOfDepartment)
class HeadOfDepartmentAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'department'
    ]
    list_filter = [
        'department__faculty'
    ]
