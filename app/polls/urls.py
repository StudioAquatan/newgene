from django.urls import path

from . import views

urlpatterns = [
    # `/polls/`
    path('', views.index, name='index'),
    path('<int:user_id>/user/', views.user, name='user'),
    path('new_user/', views.new_user, name='new_user'),
    path('<int:user_id>/send_message/', views.send_message, name='send_message'),
    path('tutorial/', views.tutorial, name='tutorial'),
]
