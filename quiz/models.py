from django.db import models

# Create your models here.
class Quiz(models.Model):
    title = models.CharField(max_length=250)
    file = models.FileField(upload_to="quiz/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title