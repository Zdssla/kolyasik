from django.urls import path
from . import views

urlpatterns = [
    path('first/', views.first, name='first'),
    path('second/', views.second, name='second'),
    path('third/', views.third, name='third'),
    path('fourth/', views.fourth, name='fourth'),
    path('courses/', views.courses, name='courses'),
    path('test/', views.test, name='test'),
    path('profile/', views.profile_view, name='profile'),
    path('save_test_result/', views.save_test_result, name='save_test_result'),
		path('doc/', views.doc, name='doc'),
]