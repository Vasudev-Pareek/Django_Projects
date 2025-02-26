from django.contrib.auth.models import User
user = User.objects.get(username='vasudevpareek')
user.set_password('123456')
user.save()


from django.contrib.auth.models import User
user = User.objects.get(username='vasudevpareek')
user.set_password('123456')
user.save()


from django.contrib.auth.models import User

# Get the user object for 'vasudevpareek'
user = User.objects.get(username='vasudevpareek')
print(user.is_superuser)  # Should print True for a superuser
print(user.is_staff)      # Should print True for accessing admin panel
user.is_superuser = True
user.is_staff = True
user.save()
