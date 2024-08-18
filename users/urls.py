from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import (
    RegisterView,
    ProfileView,
    email_verification,
    PasswordRecoveryView,
)

app_name = UsersConfig.name

urlpatterns = [
    path("login/", LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("email-confirm/<str:token>/", email_verification, name="email-confirm"),
    path("password_update/", PasswordRecoveryView.as_view(), name="password_update"),
    # path('catalog/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    # path('product_delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
]
