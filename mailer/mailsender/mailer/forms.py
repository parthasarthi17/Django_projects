from django import forms

class Email(forms.Form):
    recipient = forms.EmailField()
    message = forms.CharField()
