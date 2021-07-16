#user/models.py
from django.db import models


# Create your models here.
# 클래스 이름
# Meta: db 테이블 이름
# ORM
class UserModel(models.Model):
    class Meta:
        db_table = "my_user"

    username = models.CharField(max_length=20, null=False)
    password = models.CharField(max_length=256, null=False)
    bio = models.CharField(max_length=256, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)