from django.shortcuts import render
#from .models import Editor
from .forms import EditorForm


def index(request):
    form=EditorForm()
    context = {
    'form' : form
    }
    return render(request,'index.html',context)
