from django.shortcuts import render, redirect
from .forms import postForm
from .models import post, randompass
from django.utils.crypto import get_random_string

import random, string,uuid

def index(request):

    item_list = post.objects.order_by("-date")
    if request.method == "POST":
        form = postForm(request.POST)
        print(request.POST)

        if form.is_valid():
            obj=form.save(commit=False)
            obj.unique=uuid.uuid4()
            form.save()
            return redirect('index')
    form = postForm()
#    form.password = get_random_string(length=32)


    context = {
             "forms" : form,
             "list" : item_list,
             "title" : "randompass generator",
           }

    return render(request, 'index.html', context)
