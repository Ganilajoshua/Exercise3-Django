from django.urls import path

from .views import PostPicture 
from . import views
urlpatterns = [
    # path('post/', PostPicture.as_view(), name='PostPicture'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('post/', views.PostPicture, name='PostPicture'),
    path('post/new', views.CreatePostView, name='CreatePostView'),
    path('post/<int:pk>/edit/', views.EditPostView, name='EditPostView'),
    path('post/<pk>/remove/', views.DeletePostView, name='DeletePostView'),

    path('journal/', views.JournalView, name='JournalView'),
    path('journal/<int:pk>/edit/', views.EditJournalView, name='EditJournalView'),
    path('journal/<pk>/remove/', views.DeleteJournalView, name='DeleteJournalView'),

    path('todolist/', views.ToDoView, name='ToDoView'),
    path('todolist/<int:pk>/edit/', views.EditToDoView, name='EditToDoView'),
    path('todolist/<pk>/remove/', views.DeleteToDoView, name='DeleteToDoView'),
    path('todolist/<pk>/check/', views.FinishToDoView, name='FinishToDoView'),
    
    path('', views.MainHome, name='home') #main home
]