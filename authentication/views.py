from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import RegistrationForm

def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username', '').lower()
        password = request.POST.get('password', '')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'authentication/login.html')


def log_out(request):
    logout(request)
    return redirect('home')


def register_page(request):
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("login")
    return render(request, "authentication/register.html", {"form": form})
