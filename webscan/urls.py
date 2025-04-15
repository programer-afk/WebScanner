from django.urls import path
from django.views.generic import TemplateView


from webscan import views


urlpatterns = [
    # 欢迎页
    path('', views.welcome, name='welcome'),
    #首页
    path('index', views.index, name='index'),
    #文档页
    path('docs', views.docs, name='docs'),
    # 关于
    path('about', views.about, name='about'),
    # 端口扫描
    path('portscan', views.portscan, name='portscan'),
    #信息泄露
    path('infoleak', views.infoleak, name='infoleak'),
    #测试
    path('test', views.test, name='test'),
    path('testfp', views.testfp, name='testfp'),
    path('testfp_result', views.testfp_result, name='testfp_result'),
    #导航
    path('navigation', views.navigation, name='navigation'),
]

