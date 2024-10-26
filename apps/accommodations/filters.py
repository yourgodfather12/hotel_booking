# Path: apps/accommodations/filters.py

import django_filters
from .models import Accommodation

class AccommodationFilter(django_filters.FilterSet):
    class Meta:
        model = Accommodation
        fields = {
            'location': ['icontains'],
            'price_per_night': ['lte'],
            'rating': ['gte'],
        }
