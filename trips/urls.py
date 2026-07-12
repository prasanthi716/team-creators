from django.urls import path
from . import views

urlpatterns = [
    path("", views.fuel, name="fuel"),
]