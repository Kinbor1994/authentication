from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from .models import User

class LoginView(LoginView):
    template_name = 'accounts/login.html' 
    redirect_authenticated_user=True
