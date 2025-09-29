from django import forms
from .models import Employee
from attendances.models import Attendance

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['nik', 'name', 'position', 'email', 'phone']