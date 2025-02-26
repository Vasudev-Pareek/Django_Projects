from django.db import models

class User(models.Model):
    UID = models.CharField(max_length=100)
    uname = models.CharField(max_length=100)
    uemail = models.EmailField()
    ucontact = models.CharField(max_length=15)  # Adjust max_length based on contact format

    class Meta:
        db_table = "user"











# from django.db import models

# class User(models.Model):
#     UID = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     contact = models.CharField(max_length=15)  # Adjust max_length based on contact format

#     def __str__(self):
#         return self.name