from django.contrib import admin
from .models import Appointment

# Register the Appointment model with the admin interface
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'start_time', 'end_time')  # Display fields in the admin list view
