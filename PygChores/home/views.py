from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from rest_framework.mixins import (
    CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
)
from rest_framework.viewsets import GenericViewSet

from .models import ScheduledEvent
from .serializers import EventSerializer


class ViewSet(GenericViewSet,  # generic view functionality
                     CreateModelMixin,  # handles POSTs
                     RetrieveModelMixin,  # handles GETs for 1 Company
                     UpdateModelMixin,  # handles PUTs and PATCHes
                     ListModelMixin):  # handles GETs for many Companies

      serializer_class = EventSerializer
      queryset = ScheduledEvent.objects.all()
# Create your views here.
def main(request):
    return render(request, 'calendar/calendar.html')
# Create your views here.
