from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.
def signup(request):
    # 사용자 정보를 받아서 DB에 저장
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')

    # 사용자가 정보를 입력할 수 있는 빈종이 생성
    else:
        form = CustomUserCreationForm()

    context = {
        'form' : form,
    }
    return render(request, 'signup.html', context)

def login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        # request 인자를 넣는 이유 
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')

    else:
        form = CustomAuthenticationForm()
    context = {
        'form' : form,
    }

    return render(request, 'login.html', context)

def logout(request):
    auth_logout(request) 

    return redirect('accounts:login')

