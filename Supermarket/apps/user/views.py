"""
this is user view
                --by zero
"""

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from user.forms import RegisterForm, LoginForm, InfoForm
from user.models import Usermodel
import random

# 导入正则表达式
import re


# login/
class Loginview(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'user/login.html', {'form': form})

    def post(self, request):
        # 接收数据
        form = LoginForm(request.POST)
        # 验证数据
        res = form.is_valid()
        # 响应数据
        if res:
            # 登录成功保存session，并跳转到个人中心
            user = form.cleaned_data.get('user')
            request.session['id'] = user.id
            request.session['phone'] = user.mobile
            # 设置session 有效时间为临时
            request.session.set_expiry(0)
            return redirect(reverse('user:centent'))

        else:
            return render(request, 'user/login.html', {'form': form})


# register/

class RegisterView(View):
    # 当为get 请求时返回注册页
    def get(self, request):
        form = RegisterForm()
        return render(request, 'user/reg.html', {"form": form})

    # 当为post请求时执行
    def post(self, request):
        res = request.POST
        form = RegisterForm(res)
        data = form.is_valid()
        if data:
            form.save()
            return redirect(reverse('user:login'))
        else:
            return render(request, 'user/reg.html', {"form": form})


# centent/
class Cententview(View):
    def get(self, request):
        # 从session中获取手机号码，因为在login中已把手机号保存在session中了
        phone = request.session.get('phone')
        text = {
            'phone': phone
        }
        return render(request, 'user/member.html', text)

    def post(self, request):
        pass
        return render(request, 'user/member.html')


# address/

class Addressview(View):
    def get(self, request):
        pass
        return render(request, 'user/gladdress.html')

    def post(self, request):
        pass
        return render(request, 'user/gladdress.html')


# info/

class Infoview(View):
    def get(self, request):
        # 使用后台表单喧染前端,将数据带回到前端表单中
        form = InfoForm()
        return render(request, 'user/infor.html', {"form": form})

    def post(self, request):
        # 接收数据
        res = request.POST
        # 从session是获取登录用户的id
        id = request.session.get('id')
        # 处理数据
        form = InfoForm(res)
        re = form.is_valid()
        # 响应数据
        if re:
            # 数据合法，通过用户的ID从数据库中获取对应的用户数据
            user = Usermodel.objects.filter(pk=id)
            # 将清洗后所有数据保存在rs中
            rs = form.data
            # 更新数据库中相应的字段，数据从form表单清洗后的数据
            user.update(name=rs.get('name'), sex=rs.get('sex'), bthday=rs.get('bthday'), school=rs.get('school'),
                        address=rs.get('address'), fromshome=rs.get('fromshome'), mobile=rs.get('mobile'))
            # 更新成功后返回个人中心查看修改的数据
            return redirect(reverse('user:info'))
        else:
            # 不成功接着修改
            return render(request, 'user/infor.html', {"form": form})


# logout/
class Logoutview(View):
    def get(self, request):
        # 清除session
        request.session.flush()
        # 返回登录页
        return redirect(reverse('user:login'))

    def post(self, request):
        pass
        return HttpResponse('ok?')


# Sendcode/
class SendcodeView(View):
    # 这是get请求
    def get(self):
        pass
        return HttpResponse('ok')

    def post(self):
        return HttpResponse('ok')


"""
    发送手机验证码
"""


class SendCodeView(View):
    """
        发短信验证码
    """

    def post(self, request):
        # 获取输入的手机号
        tel = request.POST.get('tel', '')  # 默认值为空字符串
        # 导入正则表达式模块，并写规则验证是否是正确的手机号码
        phone = re.compile(r'^1[3-9]\d{9}$')
        # 通过规则匹配手机号码
        res = re.search(phone, tel)
        if res is None:
            return JsonResponse({"send": 404, 'msg': '手机号码格式错误！'})
        # 如果匹配成功，到数据库查询是否已被注册
        elif Usermodel.objects.filter(mobile=tel).exists():
            # 查询结果为TRUE
            return JsonResponse({'send': 404, 'msg': '此号码已被注册！'})
        else:
            # 允许注册，生成4位随机短信验证码
            msgcode = ''.join([str(random.randint(0, 9)) for _ in range(4)])
            return JsonResponse({'send': 200, 'msg': msgcode})


# index/

class IndexView(View):
    """
        index
    """

    def get(self, request):
        pass
        return render(request, 'index/index.html')
