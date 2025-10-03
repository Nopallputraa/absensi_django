from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Employee(models.Model):
    # Hubungkan ke User bawaan Django (opsional login untuk karyawan)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    nik = models.CharField(max_length=20, unique=True)  # Nomor induk karyawan
    name = models.CharField(max_length=120)
    position = models.CharField(max_length=120, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=30, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.nik})"

    def get_absolute_url(self):
        return reverse("employees:employee-detail", args=[self.pk])