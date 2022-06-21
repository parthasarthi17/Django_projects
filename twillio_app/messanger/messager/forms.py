from django import forms
from .models import person
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class TextForm(forms.ModelForm):
    qwertypass = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = person
        fields = ['name', 'number', 'emailid', 'qwertypass']

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = []
