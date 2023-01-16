from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseBadRequest
from django.contrib.auth import login as auth_login, logout as auth_logout


HOME_URL = 'poll:question_index'

@require_http_methods(['GET', 'POST'])
def signup(request):
    # 회원가입 > creation
    # 이미 login 한 사용자라면, 
    if request.user.is_authenticated:
        return HttpResponseBadRequest('이미 로그인 하였습니다.')
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # 회원가입 끝나자마자 로그인 시켜주기
            auth_login(request, user)
            return redirect(HOME_URL)
    else:
        form = CustomUserCreationForm()
        
    context = {'form':form, }
    return render(request, 'accounts/signup.html', context)


@require_http_methods(['GET', 'POST']) # 로그인 > authentication
def login(request):
    # login 한 사용자라면,
    if request.user.is_authenticated:
        return HttpResponseBadRequest('이미 로그인 하였습니다.')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        # 사용자가 입력한 username / password가 맞다면,
        if form.is_valid():
            # 로그인 시키기 (쿠키 세팅)
            # AuthenticationForm => User create가 아님
            # 다른 메서드 제공 (get_user)
            user = form.get_user()
            auth_login(request, user)
            return redirect(HOME_URL)
        
    else:
        form = AuthenticationForm()
    context = {'form':form, }
    return render(request, 'accounts/login.html', context)
  

def logout(request):
    auth_logout(request)
    return redirect(HOME_URL)
