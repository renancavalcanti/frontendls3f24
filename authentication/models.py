from django.db import models

# Create your models here.

class Task(models.Model):
    created_by = models.CharField(max_length=100)
    assigned_to = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    