from django.shortcuts import render, redirect
from django.contrib.auth.models import User#user에 대한 클래스 가져오기
from django.contrib import auth#계정에 대한 권한 가져오기

def signup(request):
    if request.method == 'POST':#만약에 request가 POST방식으로 들어왔다면, 회원가입전송버튼을 눌렀다면과 똑같은 의미
        if request.POST['password1'] == request.POST['password2']:#첫번째 입력한 비밀번호과 두번쨰입력한 비밀번호(확인용)이 같다면
            user = User.objects.create_user(
                username=request.POST['username'], password=request.POST['password1'])
            #아이디와, 비밀번호를 생성. User.objects.create_suer라는 함수를 그대로 사용, username과 password는 우리가 form에서 입력해준것.
            auth.login(request, user)
            return redirect('home')#위에 있는 것들이 모두 실행된다면, home으로 이동.
    return render(request, 'signup.html')#다 실패했다면, signup.html에 계속 머물도록.

def login(request):
    if request.method == 'POST':#리퀴스트메소드가 포스트방식이라면
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:#만약에 이 결과가 회원정보가 없다면, 회원이 아니라면 None을 출력하는데, 이 None이 아니라면
            auth.login(request, user)#로그인해주고
            return redirect('home')#home이라고 하는 url로 바로 리다이렉트 시켜줌.
        else:#None이라면
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})#에러를 출력해준다.
    else:
        return render(request, 'login.html')#그리고 중간에 무슨 오류가 난다면, login페이지에 그대로 머무르게  

def logout(request):
    if request.method == 'POST':#request메소드가 post방식으로 들어왔다면
        auth.logout(request)#로그아웃 함수를 실행시켜준다.
        return redirect('home')
    return render(reqeust, 'login.html')