from django.shortcuts import get_object_or_404, render
from django.utils.timezone import now
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import TestResult  # Предполагается, что есть модель TestResult для хранения результатов тестов

def first(request):
    return render(request, 'quiz/quizes/first.html')

def second(request):
    return render(request, 'quiz/quizes/second.html')

def third(request):
		return render(request, 'quiz/quizes/third.html' )

def fourth(request):
    quiz_id = 1  # Укажите ID теста, связанного с этим курсом
    return render(request, 'quiz/quizes/fourth.html', {'quiz_id': quiz_id})

def courses(request):
    return render(request, 'quiz/courses.html')

def test(request):
     return render(request, 'quiz/quizes/test.html')

def save_test_result(request):
    if request.method == 'POST':
        # Process the test result data from the request
        # Example: test_result = request.POST.get('test_result')
        # Save the data to the database or perform other logic
        return JsonResponse({'message': 'Test result saved successfully'})
    return JsonResponse({'error': 'Invalid request method'}, status=400)

@login_required
def profile_view(request):
    test_results = TestResult.objects.filter(user=request.user)  # Получение результатов текущего пользователя
    context = {
        "user": request.user,
        "test_results": test_results,  # Передача результатов теста
    }
    return render(request, "app_auth/profile.html", context)