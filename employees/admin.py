from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('nik', 'name', 'position', 'email')
    search_fields = ('nik', 'name')