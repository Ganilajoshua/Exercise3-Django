from django.shortcuts import render, redirect ,get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.shortcuts import redirect
from django.http import HttpResponse 
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.views import generic
from .models import Post,Journal,ToDoList
from .forms import PostForm,JournalForm,TodoForm
from django.contrib.auth.forms import UserCreationForm
# class PostPicture(ListView):
#     model = Post
#     template_name = 'posts/home.html'
#     def get(self, request):
#         search_term =''
#         'search' in request.GET:
#             search_term = request.GET['search']
#             model = Post.objects.filter(text__icontains=search_term)
#         return render(request, 'posts/home.html', {'posts':posts})
        

@login_required(login_url='/login/')
def PostPicture(request):
    search_term =''
    posts = Post.objects.filter(author = request.user.id)
    if 'search' in request.GET:
        search_term = request.GET['search']
        posts = Post.objects.filter(title__contains=str(search_term), author = request.user.id)
    elif request.user.is_superuser:
        posts = Post.objects.all()
    else:
        posts = Post.objects.filter(author = request.user.id)
    return render(request, 'posts/home.html', {'posts':posts})

# Picture Upload
@login_required(login_url='/login/')
def CreatePostView(request):
    if request.method == 'POST': 
        form = PostForm(request.POST, request.FILES) 
  
        if form.is_valid(): 
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/post') 
    else: 
        form = PostForm() 
    return render(request, 'posts/post.html', {'form' : form}) 

@login_required(login_url='/login/')
def EditPostView(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/post',pk=post.pk) 
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/edit.html', {'form': form})

@login_required(login_url='/login/')
def DeletePostView(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('/post')

#Journal
@login_required(login_url='/login/')
def JournalView(request): 
    if request.method == 'POST': 
        form = JournalForm(request.POST, request.FILES) 
        if form.is_valid(): 
            journal = form.save(commit=False)
            journal.author = request.user
            journal.save()
            return redirect('/journal')
            # journal.edit_date = timezone.now()
    else: 
        form = JournalForm()
        search_term =''
        journal = Journal.objects.order_by('created_date')
        search_term =''
        print(search_term)
        journal = Journal.objects.filter(author = request.user.id)
        if 'search' in request.GET:
            search_term = request.GET['search']
            journal = Journal.objects.filter(title__contains=str(search_term), author = request.user.id)
        elif request.user.is_superuser:
            journal = Journal.objects.all()
        else:
            journal = Journal.objects.filter(author = request.user.id)
        return render(request, 'journal/home.html', {'form' : form,'journal':journal}) 

@login_required(login_url='/login/')
def EditJournalView(request, pk):
    journal = get_object_or_404(Journal, pk=pk)
    if request.method == "POST":
        form = JournalForm(request.POST, request.FILES, instance=journal)
        if form.is_valid():
            journal = form.save(commit=False)
            journal.author = request.user
            journal.edit_date = timezone.now()
            journal.save()
            return redirect('/journal',pk=journal.pk) 
    else:
        form = JournalForm(instance=journal)
    return render(request, 'journal/edit.html', {'form': form})

@login_required(login_url='/login/')
def DeleteJournalView(request, pk):
    journal = get_object_or_404(Journal, pk=pk)
    journal.delete()
    return redirect('/journal')

#Todolist
@login_required(login_url='/login/')
def ToDoView(request): 
    if request.method == 'POST': 
        form = TodoForm(request.POST, request.FILES) 
        if form.is_valid(): 
            todo = form.save(commit=False)
            todo.author = request.user
            todo.save()
            return redirect('/todolist') 
            # journal.edit_date = timezone.now()
    else: 
        form = TodoForm()
        search_term =''
        todo = ToDoList.objects.order_by('created_date').filter(author = request.user.id)
        if 'search' in request.GET:
            search_term = request.GET['search']
            todo = ToDoList.objects.filter(title__contains=str(search_term), author = request.user.id)
        elif request.user.is_superuser:
            todo = ToDoList.objects.all()
        else:
            todo = ToDoList.objects.filter(author = request.user.id).order_by('created_date')
        return render(request, 'todo/home.html', {'form' : form,'todo':todo}) 

@login_required(login_url='/login/')
def EditToDoView(request, pk):
    todo = get_object_or_404(ToDoList, pk=pk)
    if request.method == "POST":
        form = TodoForm(request.POST, request.FILES, instance=todo)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.author = request.user
            todo.checkbox = false
            todo.edit_date = timezone.now()
            todo.save()
            return redirect('/todolist',pk=todo.pk) 
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todo/edit.html', {'form': form})

@login_required(login_url='/login/')
def FinishToDoView(request, pk):
    todo = get_object_or_404(ToDoList, pk=pk)
    todo.author = request.user
    todo.checkbox = False
    todo.edit_date = timezone.now()
    todo.save()
    return redirect('/todolist',pk=todo.pk) 

@login_required(login_url='/login/')
def DeleteToDoView(request, pk):
    todo = get_object_or_404(ToDoList, pk=pk)
    todo.delete()
    return redirect('/todolist')


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def MainHome(request):
    return render(request, 'home.html', {})