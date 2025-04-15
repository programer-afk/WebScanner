from django.shortcuts import render
from django.http import HttpResponse
from .models import Category,Item,PortList
from django.contrib.auth.decorators import login_required
import json
import requests
import html
# Create your views here.

def welcome(request):
    '''欢迎页'''
    return render(request, 'other/welcome.html')

def index(request):
    '''主页'''
    category_list = Category.objects.filter(add_menu=True)
    item_list = Item.objects.all()
    # cms_items = FingerPrint.objects.all()  # 已移除指纹识别相关功能
    # 取出要添加到导航栏的分类
    category_nav = Category.objects.filter(add_menu=True).order_by('sort')
    # 需要传递给模板（templates）的对象

    context ={
        'categories': category_list,
        'items': item_list,
        'category_nav': category_nav,
    }
    return render(request, 'other/index.html',context)

def about(request):
    '''关于'''
    return render(request, 'other/about.html')

def docs(request):
    '''文档'''
    return render(request, 'other/docs.html')


def navigation(request):
    '''安全导航'''
    # 取出要添加到导航栏的分类
    category_nav = Category.objects.filter(add_menu=True).order_by('sort')
    # 取出条目
    items = Item.objects.all()
    # 需要传递给模板（templates）的对象
    context = {
        'category_nav': category_nav,
        'items': items,
    }
    return render(request, 'other/navigation.html', context)

def test(request):
        return HttpResponse("Hello World!")

def testfp(request):
    '''测试页面'''
    # 取出要添加到导航栏的分类
    category_nav = Category.objects.filter(add_menu=True).order_by('sort')
    # 需要传递给模板（templates）的对象
    context = {
        'category_nav': category_nav,
    }
    return render(request, 'other/testfp.html', context)

def testfp_result(request):
    '''测试结果页面'''
    return render(request, 'other/test_result.html')

@login_required
def portscan(request):
    '''端口扫描'''
    portlists = PortList.objects.all()
    context = {'portlists': portlists}
    return render(request, 'scan/scan_portscan.html',context)


@login_required
def infoleak(request):
    '''信息泄露'''
    return render(request, 'scan/scan_infoleak.html')