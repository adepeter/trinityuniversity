from django.contrib import admin


# Register your models here.
from ..models import Course, Topic


class TopicInlineAdmin(admin.StackedInline):
    model = Topic
    extras = 2

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = [
        'code',
        'title',
        'department'
    ]
    list_filter = [
        'department'
    ]
    inlines = [TopicInlineAdmin]
