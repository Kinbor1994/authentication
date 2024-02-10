
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import User

class LoginView(LoginView):
    template_name = 'accounts/login.html' 
    redirect_authenticated_user=True

class SignUpView(CreateView):
    template_name = 'accounts/signup.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')