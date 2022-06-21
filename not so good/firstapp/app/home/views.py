from django.shortcuts import render, HttpResponse


def index(request):
    return render(request, 'index.html')

def about(request):
    return HttpResponse("work")


def service(request):
    return HttpResponse("service")


