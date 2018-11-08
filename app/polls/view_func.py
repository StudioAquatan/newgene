from .models import User, Mobile, MobileMessage


def login(username, password):
    user_id = 1
    return user_id


def get_user_context(user_id):
    login_user = User.objects.get(id=user_id)
    users_mobile = Mobile.objects.filter(user=login_user)
    message_list = MobileMessage.objects.order_by('reception_time')
    i = 0
    latest_message_list = []
    for temp_message in message_list:
        for temp_mobile in users_mobile:
            if temp_message.mobile == temp_mobile:
                latest_message_list.append(temp_message)
                i = i + 1
                break
        if i > 5:
            break

    message = MobileMessage
    context = {'latest_message_list': latest_message_list,
               'message': message, 'user_id': user_id}
    return context
