from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.views import LoginView as BaseLoginView, PasswordChangeView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from users.forms import UserRegisterForm, UserProfileForm, UserLoginForm, UserPasswordChangeForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        send_mail(
            subject='Поздравляем с регистрацией!',
            message='Вы зарегистрировались на нашей платформе, добро пожаловать!',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        return super().form_valid(form)


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')
    template_name = 'users/profile.html'

    def get_object(self, queryset=None):
        return self.request.user


class LoginView(BaseLoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm


class LogoutView(BaseLogoutView):
    pass


class UserPasswordChange(PasswordChangeView):
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy("users:password_change_done")
    template_name = "users/password_change_form.html"