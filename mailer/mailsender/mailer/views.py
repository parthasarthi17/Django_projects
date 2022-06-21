from django.shortcuts import render
from .forms import Email
from django.core.mail import send_mail
from django.conf import settings

def mailsend(request):

    MessageSent = False

    form = Email(request.POST)

    if form.is_valid():
        cd = form.cleaned_data
        subject = "Sending an email with Django"
        message = cd['message']

        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [cd['recipient']])

        MessageSent = True

    context ={
    'form' : form,
    'MessageSent' : MessageSent
    }

    return render(request, 'mailsending.html', context)
