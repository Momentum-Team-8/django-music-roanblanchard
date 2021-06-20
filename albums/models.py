from django.conf import settings
from django.db import models
from django.utils import timezone


class Album(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)

