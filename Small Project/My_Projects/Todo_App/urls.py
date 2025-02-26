from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.todo, name="todo-home"),
    path('', views.Todo_Home, name='todo-home'),
]
