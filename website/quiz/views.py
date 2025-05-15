from django.shortcuts import get_object_or_404, render
from django.utils.timezone import now
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import TestResult  # Предполагается, что есть модель TestResult для хранения результатов тестов
import json

def first(request):
    return render(request, 'quiz/quizes/first.html')

def second(request):
    return render(request, 'quiz/quizes/second.html')

def third(request):
		return render(request, 'quiz/quizes/third.html' )

def fourth(request):
    return render(request, 'quiz/quizes/fourth.html')

def courses(request):
    return render(request, 'quiz/courses.html')

def test(request):
     return render(request, 'quiz/quizes/test.html')

def doc(request):
     return render(request, 'quiz/doc.html')

@csrf_exempt
@login_required
def save_test_result(request):
    if request.method == "POST":
        data = json.loads(request.body)
        TestResult.objects.create(
            user=request.user,
            score=data.get("score", 0),
            total=data.get("total", 0)
        )
        return JsonResponse({"status": "ok"})
    return JsonResponse({"status": "error"}, status=400)

@login_required
def profile_view(request):
    # Проверка: есть ли результаты и корректно ли сортируются
    quiz_testresult = TestResult.objects.filter(user=request.user).order_by('-created_at')
    # Для отладки: можно временно вывести в консоль
    # print(list(quiz_testresult))
    context = {
        "user": request.user,
        "quiz_testresult": quiz_testresult,
    }
    return render(request, "app_auth/profile.html", context)