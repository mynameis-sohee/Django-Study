"""sparta URL Configuration
api를 관리하는 곳 = 즉, 접속할 url을 생성하고 관리하는 곳
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# views 파일을 해당 파일에 import
from . import views

# 질문: name의 역할이 무엇일까?
urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', views.base_response, name='first_test'),
    path('first/', views.first_view, name='first_view'),
    path('', include('user.urls')),
]

