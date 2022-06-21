from django.shortcuts import render, redirect

from .models import GeeksModel

def detailsviews(request, id):
    data = GeeksModel.objects.get(id=id)
    context = {
    'data':data,
    }

    return render(request,"detailsviews.html", context)


def listview(request):


    dataset = GeeksModel.objects.all()

    context = {
        'dataset' : dataset,
    }

    return render(request,"listview.html", context)
