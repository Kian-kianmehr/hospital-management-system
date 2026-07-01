from django.conf import settings
from django.db import models
from accounts.models import DoctorProfile

class Shift(models.Model):

    class ShiftStatus(models.TextChoices):
        UPCOMING = "UPCOMING", "Upcoming"
        ACTIVE = "ACTIVE", "Active"
        COMPLETED = "COMPLETED", "Completed"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="shifts"
    )

    department = models.CharField(
        max_length=100
    )

    date = models.DateField()

    start_time = models.TimeField()

    end_time = models.TimeField()

    status = models.CharField(
        max_length=20,
        choices=ShiftStatus.choices,
        default=ShiftStatus.UPCOMING
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.department} - {self.date}"


class Service(models.Model):

    specialization = models.CharField(
        max_length=30,
        choices=DoctorProfile.Specialization.choices
    )

    name = models.CharField(
        max_length=100
    )

    duration = models.PositiveIntegerField(
        help_text="Duration in minutes"
    )

    description = models.TextField(
        blank=True
    )


    def __str__(self):
        return self.name