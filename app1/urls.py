from django.urls import path

from .views import (dashboard_view, login_view, logout_view, register_view,
                    verify_otp_view)

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('verify_otp/', verify_otp_view, name='verify_otp'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard_view, name='dashboard'),
]


