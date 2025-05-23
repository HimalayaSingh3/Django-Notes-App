from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Note(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.CharField(max_length=50)

    def __str__(self):
        return self.title