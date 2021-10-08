from django.contrib import admin
from django.utils.translation import gettext_lazy as _


# Register your models here.
from ..models import Degree


@admin.register(Degree)
class DegreeAdmin(admin.ModelAdmin):
    list_display = [
        'get_degree_name',
        'programme',
        'faculty',
        'department'
    ]
    list_filter = [
        'programme',
        'faculty',
        'department'
    ]

    @admin.display(description=_('Award Name'))
    def get_degree_name(self, obj):
        return f'{obj.title} {obj.name}'
