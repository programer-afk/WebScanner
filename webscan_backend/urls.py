#-*- coding =utf-8 -*-
#@File：urls.py
#@software:PyCharm


from django.urls import path
from webscan_backend import views

urlpatterns = [
    # 端口扫描
    path('port_scan', views.port_scan, name='port_scan'),
    #信息泄露
    path('info_leak', views.info_leak, name='info_leak'),
    path('iplocating', views.iplocating, name='iplocating'),
    path('iswaf', views.is_waf, name='iswaf'),
    path('isexistcdn', views.isexistcdn, name='cdncheck'),
    path('webweight', views.webweight, name='webweight'),
    path('baseinfo', views.baseinfo, name='baseinfo'),
]

