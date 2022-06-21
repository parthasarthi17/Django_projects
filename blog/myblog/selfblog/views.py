from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post

# Create your views here.


#def front(request):
    #return render(request, 'front.html', {})

class frontView(ListView):
    model = Post
    template_name = 'front.html'

class articlesView(DetailView):
    model = Post
    template_name = 'articles.html'
