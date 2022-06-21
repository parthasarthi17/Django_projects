from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import person
from .forms import TextForm, RegisterForm
from django.utils.crypto import get_random_string
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


import random, string,uuid
# Create your views here.

def index(request):


    if request.method == 'POST':
        form = TextForm(request.POST)
        print(request.POST)

        if form.is_valid():
            obj=form.save(commit=False)


            dataset = User.objects.all()

            flag=1

            for x in dataset:
                if obj.name == x.username:
                    return HttpResponse('Username Already Exists!!!')
                    flag=0
                    break

                if obj.emailid == x.email:
                    return HttpResponse('EmailId Already Exists!!!')
                    flag=0
                    break

            if flag == 1:
                obj.unique=get_random_string(6)
                obj.save()
                return redirect('peeps',obj.name)
    form = TextForm()
    context = {
    'forms':form,
    }

    return render(request,"index.html", context)

def personview(request, name):

    data = person.objects.get(name=name)
    context = {
    'data' : data,
    }


    return render(request, 'persons.html', context)

def checkview(request, name):
    item = person.objects.get(name=name)
    qwerty = request.POST.get('Person_name')

    print(item.unique)
    print(qwerty)


    if f"{item.unique}" == qwerty:
        UUU =request.POST.get('Username')
        EEE =request.POST.get('email')
        PPPP =request.POST.get('Pass_1')

        newUser = User.objects.create(username=UUU, email=EEE, password=PPPP)
#        item.delete()
        return HttpResponse('New User Created!!')

    else:
        return HttpResponse('incorrect OTP')
