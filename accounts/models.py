from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class User(AbstractUser):

    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        DOCTOR = "DOCTOR", "Doctor"
        NURSE = "NURSE", "Nurse"
        RECEPTION = "RECEPTION", "Reception"
        PATIENT = "PATIENT", "Patient"
    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.PATIENT
    )

    phone_number = models.CharField(
        max_length=15,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.username
    

class DoctorProfile(models.Model):

    class DoctorType(models.TextChoices):
        GP = "GP", "GP"
        SPECIALIST = "SPECIALIST", "Specialist"

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="doctor_profile"
    )

    doctor_type = models.CharField(
        max_length=20,
        choices=DoctorType.choices
    )


    shift = models.CharField(
        max_length=50,
        blank=True,
        null=True   
    )
    specialization = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    medical_license_number = models.CharField(
        max_length=50,
        unique=True
    )

    department = models.CharField(
        max_length=100
    )

class NurseProfile(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="nurse_profile"
    )

    department = models.CharField(
        max_length=100
    )

    shift = models.CharField(
        max_length=50
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.user.get_full_name()