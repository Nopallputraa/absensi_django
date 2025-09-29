from django.db import models
from employees.models import Employee

class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="attendances")
    date = models.DateField()
    check_in = models.TimeField(null=True, blank=True)
    check_out = models.TimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=[
        ("Hadir", "Hadir"),
        ("Izin", "Izin"),
        ("Sakit", "Sakit"),
        ("Alpha", "Alpha"),
    ])

    def __str__(self):
        return f"{self.employee} - {self.date} ({self.status})"