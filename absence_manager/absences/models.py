# absences/models.py
from django.db import models
from django.contrib.auth.models import User

class Absence(models.Model):
    # Cambiamo il related_name in 'user_absences' per sicurezza
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_absences')
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField(blank=True, null=True)
    
    STATUS_CHOICES = [
        ('PENDING', 'In attesa'),
        ('APPROVED', 'Approvata'),
        ('REJECTED', 'Rifiutata'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)