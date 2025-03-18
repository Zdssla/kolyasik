from django.shortcuts import render, redirect
from .models import Course
from .forms import CourseForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy

from django.contrib.auth import get_user_model


User = get_user_model()


def index(request):
    title = request.GET.get('query')
    if title:
        courses = Course.objects.filter(title__icontains=title)
    else:
        courses = Course.objects.all()
    context = {'courses': courses,
               'title': title,
               }
    return render(request, 'main/index.html', context)


@login_required(login_url=reverse_lazy('login'))
def main_post(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            course = Course(**form.cleaned_data)
            course.user = request.user
            course.save()
            url = reverse('main_page')
            return redirect(url)
    else:
        form = CourseForm()
    context = {'form': form}
    return render(request, 'main/main-post.html', context)


def main_detail(request, pk):
    course = Course.objects.get(id=pk)
    context = {
        'course': course
    }
    return render(request, 'main/main.html', context)