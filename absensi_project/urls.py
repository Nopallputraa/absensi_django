from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("employees/", include("employees.urls")),
    path("attendances/", include("attendances.urls")),
    path('accounts/', include('accounts.urls')),
    path("", include("landing.urls")),
]