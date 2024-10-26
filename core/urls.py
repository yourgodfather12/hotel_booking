from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views  # Import authentication views
from apps.accommodations import views as accommodation_views  # Import the home view

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel URL
    path('accounts/login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),  # Custom login URL
    path('accounts/', include('django.contrib.auth.urls')),  # Automatically includes logout, password reset, etc.
    path('accommodations/', include('apps.accommodations.urls', namespace='accommodations')),  # Accommodations app URLs
    path('bookings/', include('apps.bookings.urls', namespace='bookings')),  # Bookings app URLs

    # Redirect root URL to the accommodations home page
    path('', accommodation_views.home, name='home'),  # Home view
]
