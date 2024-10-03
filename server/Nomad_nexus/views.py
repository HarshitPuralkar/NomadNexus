from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def index(request):
    if request.method == 'POST':
        if 'sign-up' in request.POST:
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['pass']
            password_confirmation = request.POST['pass2']
            
            # Check if the password and confirmation match
            if password == password_confirmation:
                user = User.objects.create_user(username=email, email=email, password=password)
                user.save()
                return redirect('home')  # Redirect to main website after signup

        elif 'login' in request.POST:
            email = request.POST['email']
            password = request.POST['pass']
            
            # Authenticate the user
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)  # Log the user in
                return redirect("next")  # Redirect to main website after login
            else:
                return render(request, "login.html")

    return render(request, "login.html")


def next(request):
    return render(request, "next.html")