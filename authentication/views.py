from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.views import LogoutView
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordResetView, PasswordResetConfirmView

from django.views.generic import CreateView

from django.contrib.auth.models import User

import logging

logger = logging.getLogger(__name__)


class UserLoginView(LoginView):
    template_name = 'authentication/login.html'
    success_url = reverse_lazy('books:home')


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('authentication:login')

class UserRegistrationView(CreateView):
    model = User
    form_class = RegistrationForm
    template_name = 'authentication/register.html'
    success_url = reverse_lazy('authentication:login')

class UserPasswordChangeView(PasswordChangeView):
    template_name = 'authentication/password_change.html'
    success_url = reverse_lazy('books:home')


class UserPasswordResetView(PasswordResetView):
    template_name = 'authentication/password_reset.html'
    email_template_name = 'authentication/passwor_dreset_confirm.html'
    success_url = reverse_lazy('books:home')

class UserPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'authentication/password_reset_done.html'
    success_url = reverse_lazy('authentication:login')