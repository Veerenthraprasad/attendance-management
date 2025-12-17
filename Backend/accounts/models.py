from django.contrib.auth.models import User
from django.db import models

class StaffProfile(models.Model):
    ROLE_CHOICES = [
        ('security', 'Security'),
        ('housekeeping', 'Housekeeping'),
        ('canteen', 'Canteen'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return self.user.username
