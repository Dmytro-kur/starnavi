from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Post, Like, Activity


admin.site.register(User, UserAdmin)
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Activity)