from django.shortcuts import render

from .models import Mobile, MobileMessage


def index(request):
    return render(request, 'poll/index.html')


def user(request, user_id):
    return render(request, 'poll/user.html', context)


def new_user(request):
    return render(request, 'poll/new_user.html')


def send_message(request, user_id):
    return render(request, 'poll/send_message.html')


def tutorial(request):
    return render(request, 'poll/tutorial.html')
