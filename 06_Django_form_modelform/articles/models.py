from django.db import models

# Create your models here.

class Articles(models.Model):
    title = models.TextField(max_length=10)
    content = models.TextField()
    create_at = models.TimeField(auto_now_add=True)
    updated_at = models.TimeField(auto_now=True)
    
    def __str__(self):
        return self.title