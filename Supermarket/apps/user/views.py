"""
this is user view
                --by zero
"""
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from user.forms import Userform
from user.models import Usermodel


# login/
class Loginview(View):
    def get(self, request):
        return render(request, 'user/login.html')

    def post(self, request):
        res = request.POST
        mobile = res.get('mobile')
        mobile = int(mobile)
        password = res.get('password')
        if all((mobile, password)):
            data = Usermodel.objects.filter(mobile=mobile)
            for v in data:
                if v.mobile == mobile and v.password == password:
                    #登录成功，保存session

                    return redirect(reverse('user:centent'))
                else:
                    return render(request, 'user/login.html')
        else:
            render(request, 'user/login.html')


# register/

class RegisterView(View):
    # 当为get 请求时返回注册页
    def get(self, request):
        return render(request, 'user/reg.html')

    # 当为post请求时执行
    def post(self, request):
        res = request.POST
        form = Userform(res)
        data = form.is_valid()
        if data:
            form.save()
            return redirect(reverse('user:centent'))
        else:
            data = {
                'form': form
            }
            return render(request, 'user/reg.html', data)


# centent/
class Cententview(View):
    def get(self, request):
        pass
        return render(request, 'user/member.html')

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
        return render(request, 'user/infor.html')

    def post(self, request):
        res = request.POST


        return render(request, 'user/infor.html')


# logout/
class Logoutview(View):
    def get(self, request):
        pass
        return HttpResponse('ok?')

    def post(self, request):
        pass
        return HttpResponse('ok?')
