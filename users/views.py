import random
import secrets

from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterFrom
from users.models import User


CHARS = "+-*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"


class UserLogin(LoginView):
    """Контроллер авторизации"""

    template_name = "user_login.html"
    success_url = reverse_lazy("diagnostic_center:home")


class UserLogout(LogoutView):
    """Контроллер выхода"""

    success_url = reverse_lazy("diagnostic_center:home")


class RegisterView(CreateView):
    """Контроллер регистрации пользователя"""

    model = User
    form_class = UserRegisterFrom
    template_name = "user_register.html"
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        """Отправляет письмо на почту пользователю для подтверждения email"""
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f"http://{host}/users/email-confirm/{token}"
        send_mail(
            subject="Подтверждение почты",
            message=f"Перейдите по ссылке для подтверждения почты {url}",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        return super().form_valid(form)


def email_verification(request, token):
    """Верифицирует пользователя"""
    user = get_object_or_404(User, token=token)
    if user:
        user.is_active = True
        user.save()
        return redirect(reverse("users:login"))
    else:
        return redirect(reverse("users:register"))


def res_password(request):
    """Генерирует новый пароль для пользователя и отправляет ему на почту"""
    new_password = ""
    if request.method == "POST":
        email = request.POST["email"]
        user = get_object_or_404(User, email=email)
        for i in range(10):
            new_password += random.choice(CHARS)
        send_mail(
            subject="Смена пароля",
            message=f"Новый пароль {new_password}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
        )
        user.set_password(new_password)
        user.save()
        return redirect(reverse("users:login"))
    return render(request, "reset_password.html")
