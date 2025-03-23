from django.urls import path
from .views import quiz_view, quiz_list_view

urlpatterns = [
    path('', quiz_list_view, name='courses'),  # Новый маршрут для списка курсов
    path('<int:quiz_id>/', quiz_view, name='quiz'),
]