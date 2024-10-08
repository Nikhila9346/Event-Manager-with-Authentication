from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Event(models.Model):
    event = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.event
