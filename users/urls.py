from django.urls import path
from users.apps import UsersConfig
from django.contrib.auth.views import LoginView, LogoutView
from users.views import RegisterView, email_verification, res_password

app_name = UsersConfig.name

urlpatterns = [
    path("login/", LoginView.as_view(template_name="user_login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
    path("email-confirm/<str:token>/", email_verification, name="email-confirm"),
    path("reset/", res_password, name="reset"),
]
