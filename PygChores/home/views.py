from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def main(request):
    return render(request, 'calendar/calendar.html')
# Create your views here.
