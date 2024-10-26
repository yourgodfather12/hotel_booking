from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Booking  # Replace with actual model

class BookingsListView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = 'bookings/bookings_list.html'
    context_object_name = 'bookings'
    login_url = '/login/'  # Redirects unauthenticated users to the login page

    def get_queryset(self):
        # Filter bookings by the logged-in user
        return Booking.objects.filter(user=self.request.user)
