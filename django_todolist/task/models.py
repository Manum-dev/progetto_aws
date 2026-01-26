from django.db import models
import uuid
from project.models import Project

# Create your models here.

class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50, unique=True)
    is_complete = models.BooleanField(default=False)

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="projects", null=True, blank=True)

    class Meta:
        db_table = "tasks"