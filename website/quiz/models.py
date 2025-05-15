from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Quiz(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class TestResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.PositiveIntegerField()
    total = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}: {self.score}/{self.total} ({self.created_at})"