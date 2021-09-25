from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=200)
    duration = models.IntegerField()
    frequency = models.IntegerField()
#name, duration, and frequency should come from inputted fields

class FreeTime(models.Model):
    start_time = models.DateTimeField('start_time')
    end_time = models.DateTimeField('end-time')
#start_time and end_time should come from the free time selections

class ScheduledEvent(models.Model):
    name = models.CharField(max_length=200)
    start_time = models.DateTimeField('start_time')
    end_time = models.DateTimeField('end-time')
    #event_id = models.IntegerField()
#this will be presented in the to-do list

'''
comments:
when the user adds a chore (by name, duration, and frequency) that is saved as an event
when the user changes the time for a chore as of now they are choosing themselves, but we can also provide suggestions within that day

'''