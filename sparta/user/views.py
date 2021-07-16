# render: html화면을 보여준다.
from django.shortcuts import render, redirect

# 나의 위치와 동일한 애중에 models를 갖고 온다.
from .models import UserModel

from django.http import HttpResponse
# Create your views here.
def sign_up_view(request):
    if request.method == 'GET':
        return render(request, 'user/signup.html')
    elif request.method == 'POST':
        # 방금 html에 전달한 데이터 중 username으로 된것 가져오고 없으면 None으로 저장. 이것을 username이라는 변수에 저장
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        password2 = request.POST.get('password2', None)
        bio = request.POST.get('bio', None)

        if password != password2:
            return render(request, 'user/signup.html')
        else:
            exist_user = UserModel.objects.filter(username=username)
            if exist_user:
                return render(request, 'user/signup.html')
            else:
                new_user = UserModel()
                new_user.username = username
                new_user.password = password
                new_user.bio = bio

                new_user.save()

        return redirect('/sign-in')

def sign_in_view(request):
    # 다른 페이지를 보여줄 때 redirect를 사용

    if request.method == 'POST':
        # html 특정 name의 input값을 의미한다.
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)

        # 실제 로그인하는 상대가 db에 존재하는지 확인
        me = UserModel.objects.get(username=username)
        if me.password == password:
            # session: 사용자 정보를 저장할 수 있는 공간
            # session의 user에 username을 넣는다.
            request.session['user'] = me.username
            return HttpResponse("{}님, 환영합니다.".format(username))
        else:
            return redirect(('/sign-in'))

    elif request.method == 'GET':
        return render(request, 'user/signin.html')

