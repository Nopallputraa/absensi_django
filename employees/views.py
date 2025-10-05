from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import UserPassesTestMixin
from .models import Employee
from .forms import EmployeeForm

class EmployeeListView(generic.ListView):
    model = Employee
    template_name = 'employees/employee_list.html'
    context_object_name = 'employees'
    paginate_by = 20

class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff
    def handle_no_permission(self):
        return redirect('employees:employee-list')

class EmployeeCreateView(AdminRequiredMixin, generic.CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employees/employee_form.html'

class EmployeeUpdateView(AdminRequiredMixin, generic.UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employees/employee_form.html'

class EmployeeDeleteView(AdminRequiredMixin, generic.DeleteView):
    model = Employee
    template_name = 'employees/employee_confirm_delete.html'
    success_url = reverse_lazy('employees:employee-list')

class EmployeeDetailView(generic.DetailView):
    model = Employee
    template_name = 'employees/employee_detail.html'
    context_object_name = 'employee'