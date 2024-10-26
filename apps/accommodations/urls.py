from django.urls import path
from . import views

app_name = 'accommodations'

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.advanced_search, name='advanced_search'),
    path('recommendations/', views.recommendations, name='recommendations'),
    path('<int:pk>/', views.accommodation_detail, name='accommodation_detail'),
]
