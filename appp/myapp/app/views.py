from django.shortcuts import render
from .models import post, list
from .forms import listform

# Create your views here.

def index(request):

    context ={}
    context["dataset"] = post.objects.all()

    return render(request, 'index.html', context)

def details(request, id):


    context = {}
    context["data"] = post.objects.get(id = id)

    return render(request, 'details.html', context)

def todo(request):
    item_list = list.objects.order_by("-date")
    form = listform()

    context={
            "forms" : form,
            "list" : item_list,
            "title" : "TODO LIST",
    }

    return render(request, 'todo/file.html', context)
