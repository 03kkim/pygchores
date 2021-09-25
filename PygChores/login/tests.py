from django.test import TestCase
from django.db import models
from django.contrib.auth.models import User

# Create your tests here.
class User(models.Model):
    username = models.CharField(max_length=30)
    user = User.objects.create_user()
