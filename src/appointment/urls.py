# src/appointments/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.appointment_list, name='appointment'),
]
