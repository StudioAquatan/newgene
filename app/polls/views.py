from django.shortcuts import render

from .view_func import login, get_user_context, get_send_message_context
from .models import ServerMessage, Mobile, User


def index(request):
    """
    ユーザー名とパスワードが正しければログイン
    正しくなかったり、入力漏れがあればエラーを表示
    """
    if request.method == 'POST':
        if request.POST.get('username'):
            username = request.POST.get('username')
            if request.POST.get('password'):
                password = request.POST.get('password')
                if 'btn_login' in request.POST:
                    user_id = login(username, password)
                    if user_id == -1:
                        return render(request, 'poll/index.html',
                                      {'error_message': 'ユーザー名またはパスワードが正しくありません'})
                    else:
                        context = get_user_context(user_id)
                        return render(request, 'poll/user.html', context)
                elif 'btn_sign_up' in request.POST:
                    return render(request, 'poll/new_user.html')
            else:
                return render(request, 'poll/index.html',
                              {'error_message': 'パスワードが入力されていません'})
        else:
            return render(request, 'poll/index.html',
                          {'error_message': 'ユーザー名が入力されていません'})


    return render(request, 'poll/index.html')


def userguide(request):
    return render(request, 'poll/userguide.html')


def user(request, user_id):
    context = get_user_context(user_id)
    return render(request, 'poll/user.html', context)


def new_user(request):
    return render(request, 'poll/new_user.html')


def send_message(request, user_id):
    error_message = '\0'
    if request.method == 'POST':
        if request.POST.get('user_message'):
            user_message = request.POST.get('user_message')
            login_user = User.objects.get(id=user_id)
            mobile_list = Mobile.objects.filter(user_id=login_user)
            for temp_mobile in mobile_list:
                ServerMessage.objects.create(mobile=temp_mobile,
                                             message_text=user_message)
        else:
            error_message = 'メッセージを入力してください'

    context = get_send_message_context(user_id)
    if error_message != '\0':
        context.update(error_message=error_message)
    return render(request, 'poll/send_message.html', context)


def tutorial(request):
    return render(request, 'poll/tutorial.html')
