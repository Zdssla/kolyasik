from django.urls import path
from . import views

urlpatterns = [
    path('first/', views.first_quiz, name='first'),
    path('second/', views.second_quiz, name='second'),
    path('third/', views.third_quiz, name='third'),
    path('fourth/', views.fourth_quiz, name='fourth'),
    path('courses/', views.courses, name='courses'),
    path('<int:quiz_id>/', views.quiz_view, name='quiz/1/'),  # Маршрут для теста
]