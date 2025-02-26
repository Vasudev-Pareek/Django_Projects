from django.urls import path
from . import views
# from .views import upload_view

urlpatterns = [
    path('', views.home, name='home'),
    path('FeedbackGallery', views.FeedbackGallery_view, name='FeedbackGallery'),
    path('SubmitFeedback/', views.SubmitFeedback_view, name='SubmitFeedback'),
    path('SubmitFeedback/<int:feedback_id>/', views.SubmitFeedback_view, name='SubmitFeedback'),
    # path('edit-feedback/<int:feedback_id>/', views.edit_feedback_view, name='edit_feedback'),
    path('delete-feedback/<int:id>/', views.DeleteFeedback_view, name='delete_feedback'),
    path('Thank-you-page', views.ThankYou_view, name='Thank_you_page'),

    path("upload/", views.upload_file, name="upload_file"),
    path("download/<str:filename>/", views.download_file, name="download_file"),
]
