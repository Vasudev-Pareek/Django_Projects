from django.shortcuts import render, redirect
# from django.http import HttpResponseNotAllowed, HttpResponse
from .models import User

# Create your views here.

def index(request):
    return render(request, "index.html")

def navbar(request):
    return render(request, "navbar.html")

def userreg(request):
    return render(request, "userreg.html")

def viewusers(request):
    us = User.objects.all()
    return render(request, "viewusers.html", {"userData":us})

def insertuser(request):
    vuid = request.POST['tuid']
    vuname = request.POST['tuname']
    vuemail = request.POST['tuemail']
    vucontact = request.POST['tucontact']
    us = User(UID=vuid, uname=vuname, uemail=vuemail, ucontact=vucontact)
    us.save()
    return render(request, "index.html")

def deleteProfile(request, id):
    # The get method only works when You use delete only one nbut then you delete more then one it not working and throw an error
    # us = User.objects.get(UID=id) 

    # If you want to delete more than one data then the filter() method is use 
    us = User.objects.filter(UID=id) 
    us.delete();
    return redirect("/viewusers")


def editProfile(request, id):
    us = User.objects.get(UID=id) 
    return render(request, "editProfile.html", {"user":us})




# def updateProfile(request, id):
#     newvuid = request.POST['uid']
#     newvuname = request.POST['uname']
#     newvuemail = request.POST['uemail']
#     newvucontact = request.POST['ucontact']
    
#     user = User.objects.get(UID=id)
#     user.UID = newvuid
#     user.uname = newvuname
#     user.uemail = newvuemail
#     user.ucontact = newvucontact
#     user.save()
#     return redirect("/viewusers")




def updateProfile(request, id):
    newvuid = request.POST['uid']
    newvuname = request.POST['uname']
    newvuemail = request.POST['uemail']
    newvucontact = request.POST['ucontact']

    user = User.objects.get(UID=id)
    user.UID = newvuid
    user.uname = newvuname
    user.uemail = newvuemail
    user.ucontact = newvucontact 
    user.save()
    return redirect("/viewusers")