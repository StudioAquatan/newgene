from django.shortcuts import render

from .view_func import login, get_user_context


def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if 'btn_login' in request.POST:
            user_id = login(username, password)
            context = get_user_context(user_id)
            return render(request, 'poll/user.html', context)

    return render(request, 'poll/index.html')


def user(request, user_id):
    context = get_user_context(user_id)
    return render(request, 'poll/user.html', context)


def new_user(request):
    return render(request, 'poll/new_user.html')


def send_message(request, user_id):
    return render(request, 'poll/send_message.html')


def tutorial(request):
    return render(request, 'poll/tutorial.html')
