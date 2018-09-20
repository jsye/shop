"""
this is user router
"""
from django.conf.urls import url

from user.views import RegisterView, Loginview, Cententview, Addressview, Infoview, Logoutview

urlpatterns = [
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^login/$', Loginview.as_view(), name='login'),
    url(r'^centent/$', Cententview.as_view(), name='centent'),
    url(r'^address/$', Addressview.as_view(), name='addressview'),
    url(r'^info/$', Infoview.as_view(), name='info'),
    url(r'^logout/$', Logoutview.as_view(), name='logout'),
]
