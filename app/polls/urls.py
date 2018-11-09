from django.urls import path

from . import views

urlpatterns = [
    # `/polls/`
    path('', views.index, name='index'),
    path('userguide/', views.userguide, name='userguide'),
    path('<int:user_id>/user/', views.user, name='user'),
    path('<int:user_id>/send_message_box/', views.send_message_box, name='send_message_box'),
    path('new_user/', views.new_user, name='new_user'),
    path('<int:user_id>/send_message/', views.send_message, name='send_message'),
    path('tutorial/', views.tutorial, name='tutorial'),
    path('<int:mobile_key>/m5stack_read/', views.m5stack_read, name='m5stack_read'),
    path('<int:send_mobile_key>/<int:send_msg>/<str:send_lat>/<str:send_lng>/m5stack_send/', views.m5stack_send,
         name='m5stack_send')
]
