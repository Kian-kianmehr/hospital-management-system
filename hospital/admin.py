from django.contrib import admin
from .models import Shift


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