from django.urls import path
from . import views

urlpatterns = [
    path('login_user/', views.login_user, name="login-user"),
    path('logout_user/', views.logout_user, name="logout-user"),
    path('user_register/', views.user_register, name="user-register"),
]