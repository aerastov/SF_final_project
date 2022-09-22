from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User


class UserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'phone', 'first_name', 'last_name', 'birth')


class UserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username', 'phone', 'first_name', 'last_name', 'birth')
