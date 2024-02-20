# from django.shortcuts import render
#
#
# def registration(request):
#     data = {
#         'registration_data': 'Страница регистарции'
#     }
#     return render(request, 'registration/registration.html', data)
#
#
# def signin(request):
#     data = {
#         'signin': 'Войти'
#     }
#     return render(request, 'registration/signin.html', data)
#
#
# def user_account(request):
#     data = {
#         'user_account': 'Личный кабинет'
#     }
#     return render(request, 'registration/user_account.html', data)


from django.contrib.auth.views import LoginView, TemplateView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import RegisterForm, Loginform


class RegisterCreateView(CreateView):
    form_class = RegisterForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('about')


class SignInView(LoginView):
    form_class = Loginform
    template_name = 'registration/signin.html'
    success_url = reverse_lazy('about')


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'registration/user_account.html'
    login_url = '/signin/'



