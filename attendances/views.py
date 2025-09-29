# attendances/views.py
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic, View
from django.utils import timezone
from django.db.models import Q
from django.http import HttpResponseRedirect
from .models import Attendance
from .forms import AttendanceForm
from employees.models import Employee


# List view dengan filter (nama, NIK, tanggal)
class AttendanceListView(generic.ListView):
    model = Attendance
    template_name = "attendances/attendance_list.html"
    context_object_name = "attendances"
    paginate_by = 30

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get("q")
        date = self.request.GET.get("date")
        if q:
            qs = qs.filter(
                Q(employee__name__icontains=q) |
                Q(employee__nik__icontains=q)
            )
        if date:
            qs = qs.filter(timestamp__date=date)
        return qs.select_related("employee")


# Create view (form tambah absensi)
class AttendanceCreateView(generic.CreateView):
    model = Attendance
    form_class = AttendanceForm
    template_name = "attendances/attendance_form.html"
    success_url = reverse_lazy("attendances:attendance-list")

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["employees"] = Employee.objects.all()
        return ctx


# Quick check-in/out (pakai POST sederhana)
class QuickCheckView(View):
    def post(self, request):
        emp_id = request.POST.get("employee_id")
        ct = request.POST.get("check_type", "IN")
        employee = get_object_or_404(Employee, pk=emp_id)
        Attendance.objects.create(
            employee=employee,
            check_type=ct,
            timestamp=timezone.now()
        )
        return HttpResponseRedirect(reverse("attendances:attendance-list"))