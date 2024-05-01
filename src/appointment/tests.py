# src/appointments/tests.py
from django.test import TestCase
from django.urls import reverse

class AppointmentsViewsTestCase(TestCase):
    def test_appointment_list_view(self):
        response = self.client.get(reverse('appointment_list'))
        self.assertEqual(response.status_code, 200)
