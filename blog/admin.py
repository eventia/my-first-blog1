from django.contrib import admin
from .models import Post    # 새로 만든 Post 클래스 추가

admin.site.register(Post)
