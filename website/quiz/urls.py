from django.urls import path
from .views import quiz_view, quiz_list_view

urlpatterns = [
    path('', quiz_list_view, name='courses'), 
    path('', quiz_list_view, name='first'), 
    #path('<int:quiz_id>/', quiz_view, name='quiz'),
]