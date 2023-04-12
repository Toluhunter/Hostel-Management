from django.urls import path
from . import views

app_name = "account"

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("manage/", views.AccountView.as_view(), name="account-details"),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("change-password/", views.ChangePasswordView.as_view(), name="change-password"),
    path("delete/", views.DeleteUserView.as_view(), name="delete"),
    path("", views.FetchAllUsersView.as_view(), name="fetch-users")
]
