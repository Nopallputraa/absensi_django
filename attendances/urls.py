from django.urls import path
from .views import AttendanceListView, AttendanceCreateView, QuickCheckView

app_name = "attendances"

urlpatterns = [
    path("", AttendanceListView.as_view(), name="attendance-list"),
    path("add/", AttendanceCreateView.as_view(), name="attendance-add"),
    path("quick-check/", QuickCheckView.as_view(), name="attendance-quick-check"),
]