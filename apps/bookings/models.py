# apps/bookings/models.py

from django.db import models
from apps.accommodations.models import Accommodation
from django.contrib.auth import get_user_model

class Booking(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    accommodation = models.ForeignKey(Accommodation, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking by {self.user} at {self.accommodation} from {self.check_in} to {self.check_out}"
