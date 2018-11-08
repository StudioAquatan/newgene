from django.shortcuts import render

from .view_func import login, get_user_context


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
            else:
                return render(request, 'poll/index.html',
                              {'error_message': 'パスワードが入力されていません'})
        else:
            return render(request, 'poll/index.html',
                          {'error_message': 'ユーザー名が入力されていません'})

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
