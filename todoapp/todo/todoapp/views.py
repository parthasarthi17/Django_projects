from django.shortcuts import render, redirect
from django.contrib import messages


from .forms import TodoForm
from .models import Todo


def index(request):

    item_list = Todo.objects.order_by("-date")
    form = TodoForm()

    context = {
             "forms" : form,
             "list" : item_list,
             "title" : "TODO LIST",
           }
    return render(request, 'index.html', context)
