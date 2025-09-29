# employees/views.py
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from .models import Employee
from .forms import EmployeeForm
from attendances.models import Attendance


# Employee views
class EmployeeListView(generic.ListView):
    model = Employee
    template_name = 'employees/employee_list.html'
    context_object_name = 'employees'
    paginate_by = 20

class EmployeeCreateView(generic.CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employees/employee_form.html'

class EmployeeUpdateView(generic.UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employees/employee_form.html'

class EmployeeDeleteView(generic.DeleteView):
    model = Employee
    template_name = 'employees/employee_confirm_delete.html'
    success_url = reverse_lazy('employees:employee-list')

class EmployeeDetailView(generic.DetailView):
    model = Employee
    template_name = 'employees/employee_detail.html'
    context_object_name = 'employee'