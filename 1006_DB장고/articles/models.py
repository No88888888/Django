from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Articles(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.TimeField(auto_now_add=True)
    updated_at = models.TimeField(auto_now=True)

class Comment(models.Model):
    pass
