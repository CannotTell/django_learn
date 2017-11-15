from django.shortcuts import render
from django.contrib.auth import authenticate, login
# 倒入自定义登入验证包
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q  # django并集查询
# 基于类的View
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password

from .models import UserProfile, EmailVerifyRecord
from .forms import LoginForm, RegisterForm, ForgetPwdForm
from utils.send_email import send_email
# Create your views here.


class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class ActiveUserView(View):
    def get(self, request):
        code_type = request.GET.get('type')
        code_value = request.GET.get('code')
        active_record = EmailVerifyRecord.objects.get(code=code_value, sendType=code_type)
        if active_record is not None:
            user = UserProfile.objects.get(email=active_record.email)
            user.is_active = True
            user.save()
            return render(request, 'login.html', {})
        else:
            pass
            # 处理链接错误


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'register.html', {'register_form': register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_email = request.POST.get('email', '')
            password = request.POST.get('password', '')
            user_profile = UserProfile()
            user_profile.email = user_email
            user_profile.username = user_email
            user_profile.password = make_password(password)
            user_profile.is_active = False
            user_profile.save()

            send_email(user_email)

            return render(request, 'login.html', {})
        else:
            return render(request, 'register.html', {'register_form': register_form})


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html', {})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = authenticate(username=user_name, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'index.html')
                else:
                    return render(request, 'login.html', {'msg': '用户名未激活状态，请先激活'})
            else:
                return render(request, 'login.html', {'msg': '用户名或密码错误'})
        else:
            return render(request, 'login.html', {'login_form': login_form})


class ForgetPwdView(View):
    def get(self, request):
        forget_pwd_form = ForgetPwdForm()
        return render(request, 'forgetpwd.html', {'forget_pwd_form': forget_pwd_form})

    def post(self, request):
        forget_pwd_form = ForgetPwdForm(request.POST)
        if forget_pwd_form.is_valid():
            email = request.POST.get('email', '')
            if UserProfile.objects.filter(email=email).exists():
                send_email(email, code_type='forget')
                # return render(request, 'password_reset.html', {'email': email})
            else:
                return render(request, 'forgetpwd.html', {'msg': 'email不存在'})


class ResetView(View):
    def get(self, request):
        code_type = request.GET.get('type')
        code_value = request.GET.get('code')
        active_record = EmailVerifyRecord.objects.get(code=code_value, sendType=code_type)
        if active_record is not None:
            user = UserProfile.objects.get(email=active_record.email)
            return render(request, 'password_reset.html', {'email': user.email})
        else:
            pass
            # 处理链接错误

    def post(self, request):
        pwd1 = request.POST.get('password')
        pwd2 = request.POST.get('password2')
        if pwd1 != pwd2:
            return render(request, 'password_reset.html', {'msg': '密码不一致'})
        else:
            email = request.POST.get('email')
            user = UserProfile.objects.get(email=email)
            user.password = make_password(pwd2)
            user.save()
            return render(request, 'login.html')




# def user_login(request):
#     if request.method == 'POST':
#         user_name = request.POST.get('username', '')
#         password = request.POST.get('password', '')
#         user = authenticate(username=user_name, password=password)
#         if user is not None:
#             login(request, user)
#             return render(request, 'index.html')
#         else:
#             return render(request, 'login.html', {'msg': '用户名或密码错误'})
#     elif request.method == 'GET':
#         return render(request, 'login.html', {})
