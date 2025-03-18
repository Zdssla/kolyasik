from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


User = get_user_model()

class Course(models.Model):
    title = models.CharField('Название', max_length=128)
    description = models.TextField('Описание')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
 
    def __str__(self):
        return f"Course(id={self.id}, title={self.title})"

    class Meta:
        db_table = "Users"