from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import *
import re
# from django

# Create your views here.
def home(request):
    return render(request, 'index.html')

def ThankYou_view(request):
    return render(request, 'Thank_You_Page.html')

def FeedbackGallery_view(request):
    Feedbacks = Cust_Feedback.objects.filter(is_deleted=False)
    return render(request, 'FeedbackGallery.html', {"Feedbacks":Feedbacks})


def SubmitFeedback_view(request, feedback_id=None):
    feedback = None
    
    if feedback_id:
        feedback = get_object_or_404(Cust_Feedback, id=feedback_id)

    if request.method == "POST":
        FirstName = request.POST.get('first_name', "").strip()
        LastName = request.POST.get('last_name', "").strip()
        Email = request.POST.get('email', "").strip()
        Mobile = request.POST.get('mobile', "").strip()
        Password = request.POST.get('password', "").strip()
        DateOfBirth = request.POST.get('date_of_birth', "").strip()
        Genders = request.POST.get('genders', "").strip()
        Experience = request.POST.get('experience', "").strip()
        suggestion = request.POST.get('suggestion', "").strip()
        country = request.POST.get('country', "").strip()
        user_image = request.FILES.get('user_image')

        if feedback:
            feedback.first_name = FirstName
            feedback.last_name =  LastName
            feedback.email =  Email
            feedback.mobile =  Mobile
            feedback.password =  Password
            feedback.date_of_birth =  DateOfBirth
            feedback.genders =  Genders
            feedback.experience =  Experience
            feedback.suggestion =  suggestion
            feedback.country =  country

            if user_image:
                feedback.user_image =  user_image
            feedback.save()
            messages.success(request, "Your feedback has been updated successfully.")
        else:
            if Cust_Feedback.objects.filter(email=Email).exists() or Cust_Feedback.objects.filter(mobile=Mobile).exists():
                messages.error(request, "Email or Mobile number already exists!")
                return render(request, 'SubmitFeedback.html', {"feedback": feedback}) 
            
            feedback = Cust_Feedback(
                first_name = FirstName,
                last_name =  LastName,
                email =  Email,
                mobile =  Mobile,
                password =  Password,
                date_of_birth =  DateOfBirth,
                genders =  Genders,
                experience =  Experience,
                suggestion =  suggestion,
                country =  country,
                user_image =  user_image,
            )
            feedback.save()
            messages.success(request, "Thank you! Your feedback is submitted successfully.")

        return redirect("Thank_you_page")
    
    return render(request, 'SubmitFeedback.html', {"feedback": feedback})


def DeleteFeedback_view(request, id):
    feedback = get_object_or_404(Cust_Feedback, id=id)
    feedback.is_deleted = True  # Mark as deleted
    feedback.save()
    messages.success(request, "Thank you! Your feedback is deleted successfully.", extra_tags='feedback_deleted')
    return redirect("Thank_you_page")



# azure_storage ------------------------------------>
from django.shortcuts import render
from django.http import JsonResponse
from azure.storage.blob import BlobServiceClient
from django.core.files.storage import default_storage
from django.views.decorators.csrf import csrf_exempt
import os

# Azure settings
AZURE_CONNECTION_STRING = "AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;DefaultEndpointsProtocol=http;BlobEndpoint=http://127.0.0.1:10000/devstoreaccount1;"
AZURE_CONTAINER_NAME = "storagecommoncontainer"

@csrf_exempt  # This disables CSRF for this view
def upload_file(request):
    if request.method == "POST" and request.FILES.get("file"):
        file = request.FILES["file"]
        blob_service_client = BlobServiceClient.from_connection_string(AZURE_CONNECTION_STRING)
        container_client = blob_service_client.get_container_client(AZURE_CONTAINER_NAME)

        blob_client = container_client.get_blob_client(file.name)
        blob_client.upload_blob(file, overwrite=True)

        return JsonResponse({"message": f"File '{file.name}' uploaded successfully."})
    return JsonResponse({"error": "No file provided."}, status=400)


from django.http import FileResponse, HttpResponse
from azure.storage.blob import BlobServiceClient
from io import BytesIO

def download_file(request, filename):
    blob_service_client = BlobServiceClient.from_connection_string(AZURE_CONNECTION_STRING)
    blob_client = blob_service_client.get_blob_client(AZURE_CONTAINER_NAME, filename)

    try:
        stream = blob_client.download_blob().readall()
        response = FileResponse(BytesIO(stream), as_attachment=True, filename=filename)
        return response
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}", status=404)
