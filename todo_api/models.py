from django.db import models

# Create your models here.
class Todo(models.Model):
    todo = models.CharField(max_length=120)
    completed = models.BooleanField(default=False)