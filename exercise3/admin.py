from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Post,Journal,ToDoList

admin.site.register(Post)
admin.site.register(Journal)
admin.site.register(ToDoList)