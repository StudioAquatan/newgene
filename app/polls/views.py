from django.shortcuts import render

from .view_func import login, get_user_context, get_send_message_context, get_send_message_box_context
from .models import ServerMessage, Mobile, User, MobileMessage


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


def send_message_box(request, user_id):
    context = get_send_message_box_context(user_id)
    return render(request, 'poll/send_message_box.html', context)


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
                ServerMessage.objects.create(user=login_user, mobile=temp_mobile,
                                             message_text=user_message)
        else:
            error_message = 'メッセージを入力してください'

    context = get_send_message_context(user_id)
    if error_message != '\0':
        context.update(error_message=error_message)
    return render(request, 'poll/send_message.html', context)


def tutorial(request):
    return render(request, 'poll/tutorial.html')


def m5stack_read(request, mobile_key):
    receive_mobile = Mobile.objects.get(mobile_key=mobile_key)
    server_msg = ServerMessage.objects.filter(mobile=receive_mobile).latest('send_time')
    msg = server_msg.message_text
    send_user = server_msg.user.username
    return render(request, 'poll/m5stack_read.html', {'msg': msg, 'send_user': send_user})


def m5stack_send(request, send_mobile_key, send_msg, send_lat, send_lng):
    sened_mobile = Mobile.objects.get(mobile_key=send_mobile_key)
    MobileMessage.objects.create(mobile=sened_mobile, message_text=send_msg, lat=send_lat, lng=send_lng)
    return render(request, 'poll/m5stack_send.html')
