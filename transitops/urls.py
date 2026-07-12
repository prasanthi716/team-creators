from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", include("accounts.urls")),
    path("dashboard/", include("dashboard.urls")),

    path("vehicles/", include("vehicles.urls")),

    path("drivers/", include("drivers.urls")),
    path("trips/", include("trips.urls")),
    path("fuel/", include("fuel.urls")),
    path("maintenance/", include("maintenance.urls")),
    path("reports/", include("reports.urls")),
]