from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100)
    is_Verified = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class Task(models.Model):
    AddTask = models.CharField(max_length=400)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.AddTask


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=100, null=True, blank=True, default="To Do User")
    profile_picture = models.ImageField(upload_to="profile_pics/", default="TaskManagement_App/image/download.png")

    def __str__(self):
        return self.user.username
    
