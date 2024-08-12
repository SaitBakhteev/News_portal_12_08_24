from django.shortcuts import render, redirect

from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(TemplateView, LoginRequiredMixin):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('main_page') # авторизованный пользователь попадает на главную страницу новостного портала
        return redirect('account_login') # неавторизованный пользователь попадает на страницу авторизации

# Create your views here.
