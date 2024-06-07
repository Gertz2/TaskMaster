from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Task

class CustomUserCreationForm(UserCreationForm):
    name = forms.CharField(max_length=150)

    class Meta:
        model = User    
        fields = ['username', 'name', 'password1', 'password2']

class TaskForm(forms.ModelForm):
    
    class Meta:
        model = Task
        fields = ['title', 'description', 'complete', 'due_date']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'})
        }
