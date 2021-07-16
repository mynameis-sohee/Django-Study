# django에서 어드민을 사용하겠다는 뜻
from django.contrib import admin
from .models import UserModel

# Register your models here.
admin.site.register(UserModel) # 이 코드가 나의 UserModel을 Admin에 추가 해 줍니다.