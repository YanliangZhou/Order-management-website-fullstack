from django.http import JsonResponse

from django.contrib.auth import authenticate, login, logout


# 登录处理
def signin(request):
    # 从 HTTP POST 请求中获取用户名、密码参数
    userName = request.POST.get('username')
    passWord = request.POST.get('password')

    # 使用 Django auth 库里面的 方法校验用户名、密码
    user = authenticate(username=userName, password=passWord)

    # 如果能找到用户，并且密码正确
    if user is not None:
        if user.is_active:
            if user.is_superuser:
                login(request, user)
                # 在session中存入用户类型
                request.session['usertype'] = 'mgr'

                return JsonResponse({'ret': 0})
            else:
                return JsonResponse({'ret': 1, 'msg': 'Please use administrator account to login'})
        else:
            return JsonResponse({'ret': 0, 'msg': 'User is not activated'})

    # 否则就是用户名、密码有误
    else:
        return JsonResponse({'ret': 1, 'msg': 'Incorrect user name or password'})


# 登出处理
def signout(request):
    # 使用登出方法
    logout(request)
    return JsonResponse({'ret': 0})