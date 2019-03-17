from django.db import models
from django.utils import timezone


class User(models.Model):
    """
    ユーザーのモデル
    """
    # ユーザー名
    username = models.CharField(max_length=32, unique=True)
    # パスワード
    password = models.CharField(max_length=32)


class Mobile(models.Model):
    """
    携帯端末のモデル
    """
    # ユーザーID
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # 端末登録用キー
    mobile_key = models.CharField(max_length=32, unique=True)
    # 端末所有者名
    mobile_name = models.CharField(max_length=32)


class MobileMessage(models.Model):
    """
    携帯端末からサーバへのメッセージのモデル
    """
    # 携帯端末ID
    mobile = models.ForeignKey(Mobile, on_delete=models.CASCADE)
    # 受信時刻
    reception_time = models.DateTimeField(default=timezone.now)
    # メッセージ本文
    message_text = models.CharField(max_length=50)
    # 位置情報(-1のときは位置情報なし)
    # 位置情報　緯度
    lat = models.FloatField(default=-1, blank=True, null=True)
    # 位置情報　経度
    lng = models.FloatField(default=-1, blank=True, null=True)


class ServerMessage(models.Model):
    """
    サーバから携帯端末へのメッセージのモデル
    """
    # ユーザーID
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # 携帯端末ID
    mobile = models.ForeignKey(Mobile, on_delete=models.CASCADE)
    # 送信時刻
    send_time = models.DateTimeField(default=timezone.now)
    # メッセージ本文
    message_text = models.CharField(max_length=50)
    # 位置情報(-1のときは位置情報なし)
    # 位置情報　緯度
    lat = models.FloatField(default=-1, blank=True, null=True)
    # 位置情報　経度
    lng = models.FloatField(default=-1, blank=True, null=True)
