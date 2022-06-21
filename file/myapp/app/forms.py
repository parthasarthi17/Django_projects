from django import forms
from .models import post, randompass

class postForm(forms.ModelForm):
    class Meta:
        model = post
        fields = ['title', 'email', 'date']
