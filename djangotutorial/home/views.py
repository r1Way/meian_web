from django.shortcuts import render  # 首先从django.shortcuts导入render函数



def index(request):
    # 直接使用render函数来渲染模板并返回响应
    return render(request, "home/index.html")