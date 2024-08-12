from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from .models import BaseRegisterForm
from django.shortcuts import redirect
from django.http import HttpResponseRedirect

class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/'
