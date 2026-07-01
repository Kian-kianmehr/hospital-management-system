from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class User(AbstractUser):

    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        DOCTOR = "DOCTOR", "Doctor"
        NURSE = "NURSE", "Nurse"
        PATIENT = "PATIENT", "Patient"
        RECEPTION = "RECEPTION", "Reception"
        MANAGER = "MANAGER", "Manager"
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

    class Specialization(models.TextChoices):
        GP = "GP", "General Practitioner"
        DENTIST = "DENTIST", "Dentist"
        ORTHOPEDIC = "ORTHOPEDIC", "Orthopedic"
        CARDIOLOGY = "CARDIOLOGY", "Cardiology"
        DERMATOLOGY = "DERMATOLOGY", "Dermatology"
        NEUROLOGY = "NEUROLOGY", "Neurology"
        PEDIATRICS = "PEDIATRICS", "Pediatrics"
        GYNECOLOGY = "GYNECOLOGY", "Gynecology"
        OPHTHALMOLOGY = "OPHTHALMOLOGY", "Ophthalmology"
        ENT = "ENT", "ENT"
        PSYCHIATRY = "PSYCHIATRY", "Psychiatry"


    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="doctor_profile"
    )

    specialization = models.CharField(
        max_length=30,
        choices=Specialization.choices
    )

    medical_license_number = models.CharField(
        max_length=100,
        unique=True
    )


    def __str__(self):
        return f"{self.user.username} - {self.specialization}"


class NurseProfile(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="nurse_profile"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.user.get_full_name()


class PatientProfile(models.Model):

    class Gender(models.TextChoices):
        MALE = "MALE", "Male"
        FEMALE = "FEMALE", "Female"

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="patient_profile"
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True
    )

    gender = models.CharField(
        max_length=10,
        choices=Gender.choices
    )

    phone_number = models.CharField(
        max_length=20
    )

    address = models.TextField(
        blank=True
    )

    chronic_disease_description = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.user.get_full_name()
    


class ReceptionProfile(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="reception_profile"
    )

    department = models.CharField(
        max_length=100,
        blank=True
    )

    phone_number = models.CharField(
        max_length=20
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.user.get_full_name()