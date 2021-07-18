#user/models.py
from django.db import models

# django에서 기본으로 제공하는 auth로 로그인 기능 설정
from django.contrib.auth.models import AbstractUser
# Create your models here.
# 클래스 이름
# Meta: db 테이블 이름
# ORM

# 설정 파일을 장고가 알아서 관리(4장 6번째)
from django.conf import settings


class UserModel(AbstractUser):
    class Meta:
        db_table = "my_user"
    # django 에서 기본적으로 제공하는 기능 사용하고, 추가로 bio 설정한다는 뜻
    bio = models.CharField(max_length=256, default='')
    follow = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followee')