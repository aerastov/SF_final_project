from django.contrib import admin
from .models import Post, HashTag, Comment, Likes


admin.site.register(Post)
admin.site.register(HashTag)
admin.site.register(Comment)
admin.site.register(Likes)
