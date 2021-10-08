from django.db import models


# Create your models here.
class VisitorSchedule(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    visit_date = models.DateField()
    visit_time = models.TimeField()
    has_visited = models.BooleanField(default=False)
