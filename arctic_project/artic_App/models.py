from django.db import models
from django.contrib.auth.models import User

# Create your models here.

CATEGORY_CHOICES = (
    ('ST','strawberry'),
    ('LM','lemon'),
    ('B','berry'),
)

class products(models.Model):
    image = models.ImageField(upload_to="product_img")
    name =  models.CharField(max_length=400)
    price = models.IntegerField()
    weight = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Products"  # Correct plural form


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    added_at = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Calculate total price based on quantity and product price
        self.total_price = self.product.price * self.quantity
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.user.username} - {self.product.name}"


class productnews(models.Model):
    newsImg =  models.ImageField(upload_to="productNews_img")
    newsTittle = models.CharField(max_length=200)
    newsDate = models.DateField(auto_now=True)
    newsDescription = models.CharField(max_length=500)

    def __str__(self):
        return self.newsTittle
    
    class Meta:
        verbose_name_plural = "Product News"  # Correct plural form

class shopowner(models.Model):
    ownerImg = models.ImageField(upload_to="owners_img")
    ownerName = models.CharField(max_length=200)
    ownerType = models.CharField(max_length=200)
    ownerDesc = models.CharField(max_length=500)

    def __str__(self):
        return self.ownerName
    
    class Meta:
        verbose_name_plural = "Shop Owners"  # Correct plural form


class Comment(models.Model):
    username = models.CharField(max_length=100)
    useremail = models.EmailField()
    comment_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
        # return self.comment_text[:50]

    
class CompanyLogo(models.Model):
    company_name =  models.CharField(max_length=200)
    company_logo = models.ImageField(upload_to="company_logo")

    def __str__(self):
        return self.company_name


class UserQuestios(models.Model):
    user_name = models.CharField(max_length=200)
    user_email = models.EmailField(max_length=200)
    user_phone = models.CharField(max_length=15)
    user_subject = models.CharField(max_length=400)
    user_message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_name
    
    class Meta:
        verbose_name_plural = "User Questios"
    

class BillingAddress(models.Model):
    billing_name = models.CharField(max_length=100)
    billing_email = models.EmailField()
    billing_address = models.CharField(max_length=200)
    billing_phone = models.CharField(max_length=15)
    billing_message = models.TextField()

    def __str__(self):
        return f"{self.billing_name} - {self.billing_address}"
    
    class Meta:
        verbose_name_plural = "Billing Address"
