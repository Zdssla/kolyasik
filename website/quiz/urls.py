from django.urls import path
from . import views

urlpatterns = [
    path('first/', views.first_quiz, name='first'),
    path('courses/', views.courses, name='courses'),
] 
    #path('<int:quiz_id>/', quiz_view, name='quiz'),