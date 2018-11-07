from django.shortcuts import render

from .models import Mobile, MobileMessage


def index(request):
    return render(request, 'poll/index.html')


def user(request, user_id):
    latest_message_list = MobileMessage.objects.order_by('-reception_time')[:5]
    message = MobileMessage
    mobile = Mobile
    context = {'latest_message_list': latest_message_list, 'mobile': mobile,
               'message': message, 'user_id':user_id}
    return render(request, 'poll/user.html', context)


def new_user(request):
    return render(request, 'poll/new_user.html')


def send_message(request, user_id):
    return render(request, 'poll/send_message.html')


def tutorial(request):
    return render(request, 'poll/tutorial.html')
