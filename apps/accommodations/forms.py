# Path: apps/accommodations/forms.py

from django import forms
from .models import Accommodation

class AccommodationSearchForm(forms.Form):
    location = forms.CharField(max_length=100, required=False, label="Location")
    check_in = forms.DateField(widget=forms.SelectDateWidget, required=True, label="Check-in Date")
    check_out = forms.DateField(widget=forms.SelectDateWidget, required=True, label="Check-out Date")
    guests = forms.IntegerField(min_value=1, required=True, label="Number of Guests")
