"""
this is user router
"""
from django.conf.urls import url

from user.views import RegisterView, Loginview, Cententview, Addressview, Infoview, Logoutview, SendCodeView, IndexView, \
    MessageView, ShopcartView, AllorderView, DetailView, CategoryView

urlpatterns = [
    url(r'^register/$', RegisterView.as_view(), name='register'),  # 注册
    url(r'^user/$', Loginview.as_view(), name='login'),  # 登录
    url(r'^centent/$', Cententview.as_view(), name='centent'),  # 个人中心
    # url(r'^headimg/$', headIMG, name='headimg'),  # 个人中心用户头像上传
    url(r'^address/$', Addressview.as_view(), name='addressview'),  # 收货地址
    url(r'^info/$', Infoview.as_view(), name='info'),  # 个人信息
    url(r'^logout/$', Logoutview.as_view(), name='logout'),  # 安全退出登录
    url(r'^sendcode/$', SendCodeView.as_view(), name='SendCodeView'),  # 发短信验证码
    url(r'^$', IndexView.as_view(), name='IndexView'),  # 显示index
    url(r'^message/$', MessageView.as_view(), name='MessageView'),  # 动态
    url(r'^shopcart/$', ShopcartView.as_view(), name='ShopcartView'),  # 购物车
    url(r'^allorder/$', AllorderView.as_view(), name='AllorderView'),  # 订单
    # url(r'^detail/(?P<id>\d+)/$', DetailView.as_view(), name='DetailView'),  # 详情
    url(r'^detail/$', DetailView.as_view(), name='DetailView'),  # 详情
    url(r'^category/$', CategoryView.as_view(), name='CategoryView'),  # 列表

]
