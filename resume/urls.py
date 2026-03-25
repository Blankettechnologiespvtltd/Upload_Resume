from django.urls import path
from .views import ResumeUploadAPIView

urlpatterns = [
    path('upload-resume/', ResumeUploadAPIView.as_view(), name='upload-resume'),
]