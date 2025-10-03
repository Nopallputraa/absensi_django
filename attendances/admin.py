from django.contrib import admin
from .models import Attendance, Shift


@admin.register(Shift)
class ShiftAdmin(admin.ModelAdmin):
    list_display = ("name", "start_time", "end_time")


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ("employee", "date", "status", "check_in", "check_out", "shift")
    list_filter = ("status", "shift", "date")
    search_fields = ("employee__name", "employee__nik")