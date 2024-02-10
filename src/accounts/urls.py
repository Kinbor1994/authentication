from django.urls import path

from accounts.views import LoginView, SignUpView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    # path('logout/', LogoutView.as_view(), name='logout'),
    # path('password_reset/', PasswordResetView.as_view(), name='password-reset'),
    path('signup/', SignupView.as_view(), name='signup'),
]