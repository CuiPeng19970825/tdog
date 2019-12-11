from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth import authenticate, login, logout

from .models import UserProfile

# Create your views here.


def index(request):
    return render(request, "index.html")


class LoginView(View):
    '''用户登录'''

    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        phone = request.POST.get("phone")
        pass_word = request.POST.get("password")

        try:
            # 根据手机号在db中取出相应的对象，如果不存在则返回None
            user = UserProfile.objects.get(phone=phone)

            # 效验输入的密码与数据库中该用户的密码
            if pass_word != user.password:
                user = None
            # if check_password(pass_word, user.password) is not True:
            #     user = None
            if user is not None:
                login(request, user)
                print("user{} login!".format(user.get_username()))
                return render(request, "index.html")
            else:
                return render(request, "login.html")
        except:
            return render(request, "login.html")


class RegisterView(View):
    '''用户注册'''

    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        user_name = request.POST.get("username")
        pass_word = request.POST.get("password")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        print(phone)
        print(email)
        user = UserProfile.objects.create(
            username=user_name, password=pass_word, phone=phone, email=email)
        print(user is None)
        user.is_superuser = False  # 去除管理权限
        login(request, user)
        # try:
        #     user = UserProfile.objects.create(
        #         username=user_name, password=make_password(pass_word), phone=phone, email=email)
        #     print(user is None)
        #     user.is_superuser = False
        #     login(request, user)
        # except:
        #     return render(request, 'register.html')
        return render(request, 'index.html')


def userLogout(request):
    logout(request)
    print('已退出登录')
    return render(request, "index.html")
