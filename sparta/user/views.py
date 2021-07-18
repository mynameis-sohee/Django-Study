# render: html화면을 보여준다.
from django.shortcuts import render, redirect

# 나의 위치와 동일한 애중에 models를 갖고 온다.
from .models import UserModel

from django.http import HttpResponse

# 로그아웃 기능 - 인증된 auth 정보 없애기
from django.contrib.auth.decorators import login_required

# 사용자가 DB 안에 있는지 검사 - exist_user
from django.contrib.auth import get_user_model

# post에서 작성한 password와 암호화된 password 비교 시 사용
from django.contrib import auth




# Create your views here.
def sign_up_view(request):
    if request.method == 'GET':
        user = request.user.is_authenticated  # 로그인 된 사용자가 요청하는지 검사
        # 이미 로그인한 사람이 해당 페이지 들어가지 못하도록 설정정
        # 로그인이 되어있다면
        if user:
            return redirect('/')
        else:  # 로그인이 되어있지 않다면
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
            exist_user = get_user_model().objects.filter(username=username)
            if exist_user:
                return render(request, 'user/signup.html')
            else:
                # 사용자가 있는지 알아서 확인 & 비밀번호 hash화해서 저장
                # 만약 여기서 존재한다면 알람기능을 만들고싶으면 어떻게하는가?
                UserModel.objects.create_user(username=username, password=password, bio=bio)
                return redirect('/sign-in')

def sign_in_view(request):
    # 다른 페이지를 보여줄 때 redirect를 사용

    if request.method == 'POST':
        # html 특정 name의 input값을 의미한다.
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)

        # 암호화된 password와 현재 작성한 password가 일치하는지 + 사용자가 db에 존재하는지 확인
        me = auth.authenticate(request, username=username, password=password)
        # 실제 로그인하는 상대가 db에 존재하는지 확인 - 위에서 다 했으므로 필요 X
        # me = UserModel.objects.get(username=username)

        # 암호화된 비밀번호와 비교하기 위함
        if me is not None:
            auth.login(request, me)
            # session: 사용자 정보를 저장할 수 있는 공간 - 하지만 위 django 코드가 알아서 관리하므로 주석처리
            # session의 user에 username을 넣는다.
            # request.session['user'] = me.username


            # 처음 페이지로 들어갔을 때, 로그인 정보가 있기 때문에 지정한 html로 들어가진다.
            return redirect('/')
        else:
            return redirect(('/sign-in'))

    elif request.method == 'GET':
        user = request.user.is_authenticated  # 사용자가 로그인 되어 있는지 검사
        
        # 이미 로그인한 사용자가 signin 페이지 들어가지 못하도록 설정
        if user:  # 로그인이 되어 있다면
            return redirect('/')
        else:  # 로그인이 되어 있지 않다면
            return render(request, 'user/signin.html')


# 로그아웃 - 인증된 정보를 없애기
# @login_required - 로그인 한 사용자만 접근할 수 있는 데코레이터
@login_required
def logout(request):
    auth.logout(request) # 인증 되어있는 정보를 없애기
    return redirect("/")

