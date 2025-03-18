from django import forms
from django.core.exceptions import ValidationError
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ("title", )
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'description': forms.Textarea(attrs={'class': 'form-control form-control-lg'}),        
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if title.startswith('?'):
            raise ValidationError('Заголовок не может начинаться с этого знака!')
        return title