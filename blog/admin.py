from django.contrib import admin
from .models import Post, Comment    # 새로 만든 Post 클래스 추가

admin.site.register(Post)
admin.site.register(Comment)
