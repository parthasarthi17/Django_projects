from django.shortcuts import render

from .models import GeeksModel

def detail_view(request, id):
    context ={}
    context["data"] = GeeksModel.objects.get(id = id)
    return render(request, "detail_view.html", context)
