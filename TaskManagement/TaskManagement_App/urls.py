from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('login/', views.login_attempt, name="login"),
    path('', views.register, name="register"),
    path('success/', views.success, name="success"),
    path('token/', views.token_send, name="token"),
    path('verify/<auth_token>', views.verify, name="verify"),
    path('error/', views.error, name="error"),
    path('deleteTask/<int:task_id>', views.deleteTask, name="deleteTask"),
    path('EditTask/<int:Task_id>', views.EditTask, name="EditTask"),
    path('alltask/', views.alltask_view, name="alltask"),
    path('logout/', views.logout_view, name="logout"),
    path('Profile/', views.profileEdit_view, name="Profile"),
    path('message/', views.message_view, name="message"),
    path('help/', views.help_view, name="help"),
]
