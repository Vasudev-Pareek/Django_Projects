from django.db import models

# Create your models here.

class Cust_Feedback(models.Model):
    EXPERIENCE_CHOICES = [
        ('extremely_happy', 'Extremely Happy'),
        ('happy', 'Happy'),
        ('sad', 'Sad'),
        ('very_sad', 'Very Sad'),
    ]

    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    COUNTRY_CHOICES = [
        ('India', 'India'),
        ('USA', 'USA'),
        ('UK', 'UK'),
        ('Canada', 'Canada'),
    ]

    first_name = models.CharField(max_length=50,blank=True,null=True)
    last_name = models.CharField(max_length=50, blank=True,null=True)
    email = models.EmailField()
    mobile = models.CharField(max_length=15, blank=True,null=True)
    password = models.CharField(max_length=256, blank=True,null=True)
    date_of_birth = models.DateField(blank=True,null=True)
    genders = models.CharField(max_length=20, choices=GENDER_CHOICES, blank=True,null=True)
    experience = models.CharField(max_length=20,  choices=EXPERIENCE_CHOICES, blank=True,null=True)
    suggestion = models.TextField(null=True, blank=True)
    country = models.CharField(max_length=20, choices=COUNTRY_CHOICES, blank=True,null=True)
    user_image = models.ImageField(upload_to='user_images/', null=True, blank=True, default="user_images/Avatar.png")
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"
    
