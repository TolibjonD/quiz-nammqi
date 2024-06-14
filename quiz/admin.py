from django.contrib import admin
from quiz.models import Quiz
# Register your models here.

@admin.register(Quiz)
class ModelQuizAdmin(admin.ModelAdmin):
    list_display = ['title']