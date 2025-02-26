from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password, make_password
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from .models import *
import uuid


# Create your views here.

# login_required(login_url="home")
def home(request):
    if request.method == "POST":
        Mytask = request.POST.get("Addtask")
        if Mytask:
            Task.objects.create(AddTask = Mytask)
    else:
        print("could not save")
    
    All_tasks = Task.objects.all()[:5]
    return render(request, "home.html", {'All_tasks':All_tasks})

def register(request):
    if request.method == 'POST':
        firstName = request.POST.get('firstname')
        LastName = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            if User.objects.filter(username = username).first():
                messages.success(request, "username is taken...")
                redirect("/register")

            if User.objects.filter(email = email).first():
                messages.success(request, "email is taken...")
                redirect("/register")

            user_obj = User.objects.create(username = username, email = email, first_name=firstName, last_name=LastName)
            user_obj.set_password(password)
            user_obj.save()

            auth_token = str(uuid.uuid4())
            profile_obj = Profile.objects.create(user = user_obj, auth_token = auth_token )
            profile_obj.save()
            send_mail_after_registration(email , auth_token)
            return redirect('/token')
        except Exception as e:
          print(e)
          
          
    return render(request, "register.html")

# def login(request):
#  return render(request, "login.html")

def login_attempt(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username = username).first()
        if user_obj is None:
            messages.success(request, 'User not found.')
            return redirect('/login')
        
        
        profile_obj = Profile.objects.filter(user = user_obj ).first()

        if not profile_obj.is_Verified:
            messages.success(request, 'Profile is not verified check your mail.')
            return redirect('/login')

        user = authenticate(username = username , password = password)
        if user is None:
            messages.success(request, 'Wrong password.')
            return redirect('/login')
        
        login(request , user)
        return redirect('/home')

    # return render(request , 'login.html')
    return render(request, "login.html")

def success(request):
 return render(request, "success.html")

def token_send(request):
 return render(request, "token_send.html")

def message_view(request):
    return render(request, "Message.html")

def help_view(request):
    return render(request, "help.html")

def verify(request , auth_token):
    try:
        profile_obj = Profile.objects.filter(auth_token = auth_token).first()
    

        if profile_obj:
            if profile_obj.is_Verified:
                messages.success(request, 'Your account is already verified.')
                return redirect('/success')
            profile_obj.is_Verified = True
            profile_obj.save()
            messages.success(request, 'Your account has been verified.')
            return redirect('/success')
        else:
            return redirect('/error')
    except Exception as e:
        print(e)
        return redirect('/login')



def error(request):
   return render(request, "error.html")
   
   
def send_mail_after_registration(email , token):
    subject = 'Your accounts need to be verified'
    message = f'Hi paste the link to verify your account http://127.0.0.1:8000/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message , email_from ,recipient_list )


# for log out
def logout_view(request):
    logout(request)
    return redirect("/")

 

# todo list

def deleteTask(request, task_id):
    try:
        Tasks = Task.objects.get(id=task_id)
        Tasks.delete()
    except:
        print("Task doesn't delted...")
    return redirect("/home")

def EditTask(request, Task_id):
    task = get_object_or_404(Task, id=Task_id)

    if request.method == "POST":
        UpdateTask = request.POST.get("AddTask")
        task.AddTask = UpdateTask
        task.save()
        return redirect("home")
    
    return render(request, "Edit_Task.html", {"tasks":task})

def alltask_view(request):
    tasks = Task.objects.all()
    return render(request, "All_task.html", {'tasks':tasks})



# Profile edit
def profileEdit_view(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        bio = request.POST.get("bio")
        profile_picture = request.FILES.get("profile_picture")

        user_profile.bio = bio
        if profile_picture:
            user_profile.profile_picture = profile_picture

        user_profile.save()

        return redirect("Profile")
    # else:
    #     user_profile, created = UserProfile.objects.get_or_create(user = request.user )
    return render(request, "Profile_Edit.html", {"user_profile":user_profile})


def change_password(request):
    if request.method == 'POST':
        CP = request.POST.get("CurrentPassword")
        NP = request.POST.get("NewPassword")
        VF = request.POST.get("VerifyPassword")

        if CP and NP and VF:
            if check_password(CP, request.user.password):
                if NP == VF:
                    request.user.password = make_password(NP)
                    request.user.save()
                    messages.success(request, "Password successfully changed!")
                else:
                    messages.error(request, "New password and Verify password do not match.")
            else:
                    messages.error(request, "Current password is incorrect.")




            

