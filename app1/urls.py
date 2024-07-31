# accounts/urls.py
from django.urls import path

from . import views  # Import views from the current app
from .views import dashboard_view, register_view

urlpatterns = [
    path('login/', views.login_view, name='login'),  # Login view
    path('register/', views.register_view, name='register'),  # Registration view
    path('logout/', views.logout_view, name='logout'),  # Logout view
    path('dashboard/', dashboard_view, name='dashboard'),
    # Add more paths as needed
]


