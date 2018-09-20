"""
this is user view
"""
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


# login/
class Loginview(View):
    def get(self, request):
        pass
        return render(request, 'user/login.html')

    def post(self, request):
        pass
        return render(request, 'user/login.html')


# register/

class RegisterView(View):
    def get(self, request):
        pass
        return render(request, 'user/reg.html')

    def post(self, request):
        pass
        return render(request, 'user/reg.html')


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
        pass
        return render(request, 'user/infor.html')

    def post(self, request):
        pass
        return render(request, 'user/infor.html')


# logout/
class Logoutview(View):
    def get(self, request):
        pass
        return HttpResponse('ok?')

    def post(self, request):
        pass
        return HttpResponse('ok?')
