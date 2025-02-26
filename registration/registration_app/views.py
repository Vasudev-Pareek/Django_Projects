from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required(login_url="login")
def HomePage(request):
    return render(request, "home.html")

def SignupPage(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        if password1!=password2:
            return HttpResponse("Your Password and confirm password is not same !!!")
        my_user = User.objects.create_user(uname, email, password1)
        my_user.save()
        return redirect("/Login")
    return render(request, "signup.html")

def LoginPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        pass1 = request.POST.get("pass")
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect("Home")
        else:
            return redirect("Username or Password is incorrect")
    return render(request, "login.html")

def LogoutPage(request):
    logout(request)
    return redirect("login")