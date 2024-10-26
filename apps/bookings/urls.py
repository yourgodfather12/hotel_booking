from django.urls import path
from . import views

app_name = 'bookings'

urlpatterns = [
    path('list/', views.BookingsListView.as_view(), name='list'),
]
