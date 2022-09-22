from django.db import models
from .validators import validate_tg

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from .manager import UserManager


class User(AbstractBaseUser, PermissionsMixin):

    first_name = models.CharField(_('Имя'), max_length=30, blank=True)
    last_name = models.CharField(_('Фамилия'), max_length=30, blank=True)
    username = models.CharField(_('Логин'), max_length=30, unique=True)
    email = models.EmailField(_('email'), unique=True)
    phone = PhoneNumberField(_('Телефон'),unique=True)
    tg = models.CharField(_('Телеграм'), max_length=64, validators=[validate_tg], blank=True)
    birth = models.DateField(_('День рождения'), null=True, blank=True)
    date_joined = models.DateTimeField(_('Зарегистрирован'), auto_now_add=True)
    is_active = models.BooleanField(_('is_active'), default=True)
    is_staff = models.BooleanField(_('staff status'), default=False)
    avatar = models.ImageField(upload_to='avatars/', verbose_name='Фото профиля',
                               default='avatars/default.jpg', null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone']

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
