from django.shortcuts import get_object_or_404, render
from .models import Quiz, Question, Answer

def quiz_view(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)  # Получение викторины по ID
    if request.method == 'POST':
        score = 0
        for question in quiz.questions.all():
            selected_answer_id = request.POST.get(str(question.id))
            if selected_answer_id:
                selected_answer = Answer.objects.get(id=selected_answer_id)
                if selected_answer.is_correct:
                    score += 1
        return render(request, 'quiz/result.html', {'quiz': quiz, 'score': score})
    return render(request, 'quiz/quiz.html', {'quiz': quiz})

def quiz_list_view(request):
    quizzes = Quiz.objects.all()  # Получаем все викторины
    return render(request, 'quiz/courses.html', {'quizzes': quizzes})

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