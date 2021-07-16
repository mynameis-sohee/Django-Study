# admin 페이지에 생성한 TweetModel 넣기
# 데이터 수정 및 추가 삭제할 때 이 admin 페이지를 이용하면 된다.
from django.contrib import admin
from .models import TweetModel

# Register your models here.
admin.site.register(TweetModel)