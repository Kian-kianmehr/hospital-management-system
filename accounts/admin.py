from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, DoctorProfile, NurseProfile, PatientProfile, ReceptionProfile


@admin.register(User)
class CustomUserAdmin(UserAdmin):

    fieldsets = (
        (None, {
            "fields": (
                "username",
                "password",
            )
        }),
        ("Personal info", {
            "fields": (
                "first_name",
                "last_name",
                "email",
                "phone_number",
            )
        }),
        ("Role", {
            "fields": (
                "role",
            )
        }),
        ("Permissions", {
            "fields": (
                "is_active",
                "is_staff",
                "is_superuser",
                "groups",
                "user_permissions",
            )
        }),
        ("Important dates", {
            "fields": (
                "last_login",
                "date_joined",
            )
        }),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "username",
                "password1",
                "password2",
                "role",
                "phone_number",
            ),
        }),
    )

    list_display = (
        "username",
        "email",
        "role",
        "is_staff",
    )

@admin.register(DoctorProfile)
class DoctorProfileAdmin(admin.ModelAdmin):

    fieldsets = (
        ("Doctor Information", {
            "fields": (
                "user",
                "doctor_type",
                "specialization",
                "shift",
            )
        }),

        ("Professional Information", {
            "fields": (
                "medical_license_number",
                "department",
            )
        }),
    )

    list_display = (
        "user",
        "doctor_type",
        "specialization",
        "department",
        "shift",
        "medical_license_number",
    )

    search_fields = (
        "user__username",
        "medical_license_number",
    )


@admin.register(NurseProfile)
class NurseProfileAdmin(admin.ModelAdmin):

    fieldsets = (
        ("Nurse Information", {
            "fields": (
                "user",
                "department",
                "shift",
            )
        }),
    )

    list_display = (
        "user",
        "department",
        "shift",
    )

    search_fields = (
        "user__username",
    )


@admin.register(PatientProfile)
class PatientProfileAdmin(admin.ModelAdmin):

    fieldsets = (
        ("Patient Information", {
            "fields": (
                "user",
                "date_of_birth",
                "gender",
                "phone_number",
                "address",
            )
        }),

        ("Medical Information", {
            "fields": (
                "chronic_disease_description",
            )
        }),
    )

    list_display = (
        "user",
        "gender",
        "phone_number",
        "date_of_birth",
    )

    search_fields = (
        "user__username",
        "phone_number",
    )

@admin.register(ReceptionProfile)
class ReceptionProfileAdmin(admin.ModelAdmin):

    fieldsets = (
        ("Reception Information", {
            "fields": (
                "user",
                "department",
                "phone_number",
            )
        }),
    )

    list_display = (
        "user",
        "department",
        "phone_number",
    )

    search_fields = (
        "user__username",
        "phone_number",
    )