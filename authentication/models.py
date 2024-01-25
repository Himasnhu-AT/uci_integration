from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models

# update model

class Subscription(models.Model):
    name = models.CharField(max_length=255)
    org = models.CharField(max_length=255)

class User(AbstractUser):
    subscription = models.ManyToManyField(Subscription)
    org = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    preferences = models.CharField(max_length=255)