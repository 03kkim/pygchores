from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=200)
    duration = models.IntegerField()
    frequency = models.IntegerField()

class FreeTime(models.Model):
    start_time = models.DateTimeField('start_time')
    end_time = models.DateTimeField('end-time')