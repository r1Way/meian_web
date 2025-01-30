from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect  # 首先从django.shortcuts导入render函数
from .forms import LoginForm, RegisterForm


def index(request):
    # 直接使用render函数来渲染模板并返回响应
    context = {
        'user': request.user
    }
    return render(request, "home/index.html", context)

def findmeian(request):
    context = {
        'user': request.user
    }
    return render(request,"home/findmeian.html", context)

def about(request):
    context = {
        'user': request.user
    }
    return render(request,"home/about.html", context)

def freetotalk_view(request):
    context = {
        'user': request.user
    }
    return render(request,'home/freetotalk.html', context)

def question_view(request):
    context = {
        'user': request.user
    }
    return render(request,'home/question.html', context)

#登录界面
def login_view(request):
    if request.method != 'POST':
        form = LoginForm()
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('../')
            else:
                return HttpResponse('登录失败')
    context = {'form': form}
    return render(request, 'home/login.html', context)

#注册界面
def register_view(request):
    if request.method != 'POST':
        form =RegisterForm()
    else:
        form=RegisterForm(request.POST)
        if form.is_valid():
            new_user=form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            # return redirect('/login')
            return HttpResponse('注册成功')
    context = {'form': form}
    return render(request, 'home/register.html',context)

