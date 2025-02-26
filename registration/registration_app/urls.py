from django.urls import path, include
from . import views

urlpatterns = [
    path('Home/', views.HomePage, name="Home" ),
    path('', views.SignupPage, name="signup" ),
    path('Login/', views.LoginPage, name="login" ),
    path('Logout/', views.LogoutPage, name="logout" ),
]