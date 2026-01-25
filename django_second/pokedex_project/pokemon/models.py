from django.db import models
import uuid

# Create your models here.
class Pokemon (models.Model):
    name = models.CharField(max_length=100)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pokedex_id = models.IntegerField()
def __str__(self):
        return self.name