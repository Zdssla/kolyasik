from django.shortcuts import render
from .models import Quiz, Question, Answer

def quiz_view(request, quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
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

def first_quiz(request):
    return render(request, 'quiz/quizes/first.html')

def courses(request):
    return render(request, 'quiz/courses.html')