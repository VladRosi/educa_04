from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView


def logout_view(request):
  logout(request)
  return render(request, 'registration/logged_out.html')


