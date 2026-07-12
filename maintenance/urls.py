from django.urls import path
from . import views

urlpatterns = [
    path('', views.MaintenanceListView.as_view(), name='maintenance_list'),
    path('create/', views.MaintenanceCreateView.as_view(), name='maintenance_create'),
    path('<int:pk>/edit/', views.MaintenanceUpdateView.as_view(), name='maintenance_update'),
    path('<int:pk>/close/', views.close_maintenance, name='maintenance_close'),
    path('<int:pk>/delete/', views.MaintenanceDeleteView.as_view(), name='maintenance_delete'),
]
