from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout

from django.http import JsonResponse
import re

def remove_email_domain(email):
    if '@' in email:
        return email.split('@')[0]
    return email

def login(request):
    if request.method == 'POST':
        if 'sign-up' in request.POST:
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['pass']
            password_confirmation = request.POST['pass2']

            if password == password_confirmation:
                user = User.objects.create_user(username=email, email=email, password=password)
                user.save()
                return redirect('home')

        elif 'login' in request.POST:
            email = request.POST.get('email')
            password = request.POST.get('pass')

            if email and password:  # Check if fields are not empty
                user = authenticate(request, username=email, password=password)
                if user is not None:
                    auth_login(request, user)
                    return redirect("home")
                else:
                    context = {'error': 'Invalid email or password.'}
                    return render(request, "login.html", context)

    return render(request, "login.html")

def home(request):
    username = remove_email_domain(request.user.username) 
    context = {'username': username}
    return render(request, "homepage.html", context)

def flights(request):
    return render(request, "flights.html")

def buses(request):
    return render(request, "buses.html")

def trains(request):
    return render(request, "trains.html")

def itenary(request):
    return render(request, "itenary.html")

def add_itenary(request):
    return render(request, "add_itenary.html")

def payment_gateway(request):
    return render(request, "payment-gateway.html")

def payment(request):
    return render(request, "payment.html")

def logout_view(request):
    logout(request)  # Log the user out
    return redirect('home')

def dynamic_label_view(request):
    return render(request, 'pup.html', {'message': "hahaha"})

def update_label(request):
    input_text = request.GET.get('input_text', '')
    res = check_password_against_conditions(input_text)
        
    return JsonResponse({'label_text': res})

def check_password_against_conditions(input):
    if len(input) < 8:
        return "Password must be at least 8 characters long."
    
    if not re.search(r'[A-Z]', input):
        return "Password must contain at least one uppercase letter."
    
    if not re.search(r'[a-z]', input):
        return "Password must contain at least one lowercase letter."
    
    if not re.search(r'\d', input):
        return "Password must contain at least one digit."
    
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', input):
        return "Password must contain at least one special character."
    
    return "Password is valid."