from django.contrib import admin
from .models import Shift, Service, SymptomCheck


@admin.register(Shift)
class ShiftAdmin(admin.ModelAdmin):

    fieldsets = (
        ("Shift Information", {
            "fields": (
                "user",
                "department",
                "date",
                "start_time",
                "end_time",
                "status",
            )
        }),
    )

    list_display = (
        "user",
        "department",
        "date",
        "start_time",
        "end_time",
        "status",
    )

    search_fields = (
        "user__username",
        "department",
    )

    list_filter = (
        "department",
        "status",
        "date",
    )


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):

    fieldsets = (
        ("Service Information", {
            "fields": (
                "name",
                "specialization",
                "duration",
                "description",
            )
        }),
    )

    list_display = (
        "name",
        "specialization",
        "duration",
    )

    search_fields = (
        "name",
    )

    list_filter = (
        "specialization",
    )




@admin.register(SymptomCheck)
class SymptomCheckAdmin(admin.ModelAdmin):

    list_display = (
        "patient",
        "suggested_specialization",
        "severity",
        "created_at",
    )

    list_filter = (
        "severity",
        "created_at",
    )

    search_fields = (
        "patient__user__username",
        "symptoms",
        "suggested_specialization",
    )