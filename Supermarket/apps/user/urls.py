"""
this is user router
"""
from django.conf.urls import url

from user.views import RegisterView, Loginview, Cententview, Addressview, Infoview, Logoutview, SendCodeView

urlpatterns = [
    url(r'^register/$', RegisterView.as_view(), name='register'),  # 注册
    url(r'^login/$', Loginview.as_view(), name='login'),  # 登录
    url(r'^centent/$', Cententview.as_view(), name='centent'),  # 个人中心
    url(r'^address/$', Addressview.as_view(), name='addressview'),  # 收货地址
    url(r'^info/$', Infoview.as_view(), name='info'),  # 个人信息
    url(r'^logout/$', Logoutview.as_view(), name='logout'),  # 安全退出登录
    url(r'^sendcode/$', SendCodeView.as_view(), name='SendCodeView'),  # 发短信验证码
]
