from django.shortcuts import render
from django.http import HttpResponse
from .models import Appointment

def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointment/index.html', {'appointments': appointments})
