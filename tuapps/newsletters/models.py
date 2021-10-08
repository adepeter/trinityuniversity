from django.db import models


# Create your models here.

class Newsletter(models.Model):
    date_posted = models.DateTimeField(auto_now_add=True)


class Subscriber(models.Model):
    subscriber_email = models.EmailField(unique=True)
    date_subscribed = models.DateTimeField(auto_now_add=True)
    

class Subscription(models.Model):
    pass
