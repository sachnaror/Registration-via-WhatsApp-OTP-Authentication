import random

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from .models import Registration
from .utils import send_whatsapp_otp


def generate_otp():
    return str(random.randint(100000, 999999))

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('register')

        # Save the user details
        user = User.objects.create_user(username=username, email=email, password=password)
        user.is_active = False  # Disable account until OTP is verified
        user.save()

        # Generate OTP and send via WhatsApp
        otp_code = generate_otp()
        Registration.objects.create(user=user, phone=phone, otp_code=otp_code)

        send_whatsapp_otp(phone, otp_code)

        request.session['user_id'] = user.id
        request.session['otp_code'] = otp_code

        messages.success(request, 'OTP sent to your WhatsApp.')
        return redirect('verify_otp')
    return render(request, 'app1/register.html')

def verify_otp_view(request):
    if request.method == 'POST':
        entered_otp = request.POST.get('otp')
        user_id = request.session.get('user_id')
        otp_code = request.session.get('otp_code')

        if user_id and entered_otp == otp_code:
            user = User.objects.get(id=user_id)
            user.is_active = True
            user.save()

            # Clear session data
            del request.session['user_id']
            del request.session['otp_code']

            messages.success(request, 'OTP verified successfully. You can now login.')
            return redirect('login')
        else:
            messages.error(request, 'Invalid OTP. Please try again.')
    return render(request, 'app1/verify_otp.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.is_active:
                login(request, user)
                messages.success(request, 'Logged in successfully.')
                return redirect('dashboard')
            else:
                messages.error(request, 'Account not activated. Please verify your OTP.')
                return redirect('login')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'app1/login.html', {'form': form})

def dashboard_view(request):
    return render(request, 'app1/dashboard.html')
