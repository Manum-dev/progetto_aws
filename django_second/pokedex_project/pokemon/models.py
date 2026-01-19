from django.db import models

# Create your models here.
class Pokemon (models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    levels = models.IntegerField(default=1)
    descriptions = models.TextField(blank=True)

def __str__(self):
        return self.name