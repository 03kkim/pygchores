from django.contrib import admin

# Register your models here.
from .models import ScheduledEvent

admin.site.register(ScheduledEvent)