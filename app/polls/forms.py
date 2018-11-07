from django import forms
from .models import Mobile, User


class RegistrationForm(forms.ModelForm):
    """
    新規登録用フォーム
    """

    class Meta:
        model = User,
        fields = ('username', 'password')


class MobileForm(forms.ModelForm):
    """
    携帯端末登録用フォーム
    """

    class Meta:
        model = Mobile,
        fields = ('mobile_key', 'mobile_name')


class LoginForm(forms.Form):
    """
    ログイン用フォーム
    """
    username = forms.CharField()
    password = forms.CharField()
