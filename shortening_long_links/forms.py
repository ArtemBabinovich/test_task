from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from shortening_long_links.models import Links


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class UrlForm(forms.ModelForm):

    class Meta:
        model = Links
        fields = ('links',)
