from django.db import models
from django.contrib.auth.models import User

class LeaveRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=20, default="Pending")

    def __str__(self):
        return f"{self.user.username} - {self.status}"
