from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def main(request):
    template = loader.get_template('login/index.html')
    return render(request, 'login/index.html')