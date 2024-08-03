# app1/views.py

import random

from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import CustomUser, LoginForm
from .models import CustomUser
from .utils import send_otp_to_whatsapp
from .whatsapp_utils import send_otp_to_whatsapp


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('dashboard')  # Redirect to dashboard after successful login
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})




def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            phone_number = form.cleaned_data.get('phone_number')
            password = form.cleaned_data.get('password')

            # Check if username or email already exists
            if CustomUser.objects.filter(username=username).exists():
                messages.error(request, "Username already exists.")
                return redirect('register')
            if CustomUser.objects.filter(email=email).exists():
                messages.error(request, "Email already exists.")
                return redirect('register')

            # Create and save the user
            user = form.save(commit=False)
            user.set_password(password)
            user.save()

            # Generate OTP and send it via WhatsApp
            otp = random.randint(100000, 999999)
            send_otp_to_whatsapp(phone_number, otp)

            # Store OTP and phone number in session for verification
            request.session['otp'] = otp
            request.session['phone_number'] = phone_number

            return redirect('verify_otp')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})
def verify_otp_view(request):
    if request.method == 'POST':
        otp_code = request.POST.get('otp_code')
        session_otp = request.session.get('otp')
        phone_number = request.session.get('phone_number')

        if str(otp_code) == str(session_otp):
            # Mark the user as verified in the CustomUser model
            user = CustomUser.objects.get(phone_number=phone_number)
            user.otp_verified = True
            user.save()
            messages.success(request, 'OTP verified successfully.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid OTP code.')

    return render(request, 'verify_otp.html')

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'Logged out successfully.')
        return redirect('login')
    return render(request, 'app1/logout.html')

@login_required
def dashboard_view(request):
    return render(request, 'dashboard.html')
