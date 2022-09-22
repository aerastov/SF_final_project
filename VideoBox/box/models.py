from django.db import models
from accounts.models import User

# Пользователь;
# Видеоролик;
# Комментарий;
# Подписка;
# Бан/игнор;
# Лайк.


class Post(models.Model):
    video = models.CharField(verbose_name='Ссылка на видео', max_length=400, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    dateCreation = models.DateTimeField(auto_now_add=True)
    dateEdit = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=256, verbose_name='Название')
    description = models.CharField(max_length=512, verbose_name='Описание:')
    text = models.TextField(verbose_name='Текст')
    is_archive = models.BooleanField(default=False, verbose_name='Архив')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class HashTag(models.Model):
    name = models.CharField(max_length=32, unique=True)
    post = models.ManyToManyField(Post)

    def __str__(self):
        return self.name


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Содержание')
    is_active = models.BooleanField(default=True, verbose_name='Выводить на экран?')
    dateCreation = models.DateTimeField(auto_now_add=True, verbose_name='Опубликован')
    dateEdit = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Комментарии'
        verbose_name = 'Комментарий'
        ordering = ['dateCreation']


class Likes(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    like = models.SmallIntegerField(default=0)
    dateCreation = models.DateTimeField(auto_now_add=True, verbose_name='Опубликован')
    dateEdit = models.DateTimeField(auto_now=True)

class Subscription(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} подписан на {self.author}'

class Ban(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=512, verbose_name='Причина')
    dateCreation = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    duration = models.IntegerField(default=0, blank=True)
