from django.conf.urls import re_path, include
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ViewSet

from . import views

router = DefaultRouter()
router.register('test', ViewSet, basename='event')

urlpatterns = [
    path('', views.main, name='main'),
    re_path(r'^service/', include(router.urls)),
]