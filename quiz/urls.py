from django.urls import path
from .views import UploadQuiz

urlpatterns = [
    path("quiz-upload-html-session-only-Admin-access/", UploadQuiz.as_view(), name="upload-quiz")
]
