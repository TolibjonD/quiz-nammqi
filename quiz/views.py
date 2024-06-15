from django.shortcuts import render, redirect
from django.views import View
from .forms import QuizForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Quiz
from file_reader import file_reader
from hitcount.models import HitCount
from hitcount.views import HitCountMixin

# Create your views here.
def index(request):
    if request.GET.get('index'):
        index = int(request.GET.get('index'))
    else:
        index=0
    titles = Quiz.objects.all()
    A = []
    for i in titles:
        A.append(i.title)
    if int(index) < 0 or int(index) > len(titles):
        index=0
        quiz = Quiz.objects.all()[0]
    else:
        if index > 0:
            quiz = Quiz.objects.all()[index-1]
        else:
            quiz = Quiz.objects.all()[0]
    hit_count = HitCount.objects.get_for_object(quiz)
    hit_count_response = HitCountMixin.hit_count(request, hit_count)
    data = file_reader(quiz.file.path)
    context = {
        "title": quiz.title,
        "data": data,
        "categories": A,
        "quiz": quiz,
        "index": int(index)
    }
    return render(request, "index.html", context)


class UploadQuiz(LoginRequiredMixin, View):
    def get(self, request):
        form = QuizForm()
        return render(request, "admin/upload.html", {"form": form})
    
    def post(self, request):
        form = QuizForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("index")
        return render(request, "admin/upload.html", {"form": form})