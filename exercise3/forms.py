from django import forms
from .models import Post,Journal,ToDoList

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title','text','cover']

class JournalForm(forms.ModelForm):

    class Meta:
        model = Journal
        fields = ['title','text']

class TodoForm(forms.ModelForm):

    class Meta:
        model = ToDoList
        fields = ['title']