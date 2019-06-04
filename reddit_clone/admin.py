from django.contrib import admin
from .models import Post, Comment, User

admin.site.register(User)
admin.site.register(Comment)
