from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, DoctorProfile


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
        "medical_license_number",
    )

    search_fields = (
        "user__username",
        "medical_license_number",
    )