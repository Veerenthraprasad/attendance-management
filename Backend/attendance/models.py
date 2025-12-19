from django.db import models
from django.utils import timezone
from django.conf import settings


class Attendance(models.Model):

    STATUS_CHOICES = [
        ("COMPLETED", "Completed"),
        ("INCOMPLETE", "Incomplete"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="attendances"
    )

    check_in_time = models.DateTimeField(default=timezone.now)
    check_out_time = models.DateTimeField(null=True, blank=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="INCOMPLETE"
    )

    force_closed = models.BooleanField(default=False)
    admin_override = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def is_checked_out(self):
        return self.check_out_time is not None

    def __str__(self):
        return f"{self.user.user_id} - {self.check_in_time.date()}"
