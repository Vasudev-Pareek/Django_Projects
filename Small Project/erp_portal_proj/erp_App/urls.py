from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('navbar/', views.navbar, name="navbar"),
    path('userreg/', views.userreg, name="userreg"),
    path('insertuser/', views.insertuser, name="insertuser"),
    path('viewusers/', views.viewusers, name="viewusers"),
    path('deleteProfile/<int:id>', views.deleteProfile, name="deleteProfile"),
    path('updateProfile/<int:id>', views.updateProfile, name="updateProfile"),
    path('editProfile/<int:id>', views.editProfile, name="editProfile"),
]
