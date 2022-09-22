from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .forms import UserCreationForm, UserChangeForm
from .models import User


class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ('username', 'is_staff', 'is_active', 'date_joined') # поля, отображаемые в списке пользователей
    list_filter = ('is_staff', 'is_active',) # поля, по которым можно фильтровать
    fieldsets = (
        (None, {'fields': ('username', 'phone', 'first_name', 'last_name', 'birth', 'password')}),
        (_("Personal info"), {"fields": ("tg", "email")}),
        (_("Permissions"), {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions",),},),
        (_("Important dates"), {"fields": ("last_login", )}),
        (_("Фотография"), {"fields": ("avatar",)}),
    )
    add_fieldsets = (
        (None, {'classes': ('wide',), 'fields': ('username', 'phone', 'name', 'birth', 'password1', 'password2', 'is_staff', 'is_active',),},),
    )
    search_fields = ('username',)
    ordering = ('username',)

admin.site.register(User, UserAdmin)