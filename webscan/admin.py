from django.contrib import admin

from .models import Category,Item,PortList
from import_export.admin import ImportExportModelAdmin
from django.db import models
from django.forms import TextInput
# Register your models here.

#修改后台管理页面头部显示内容和后台名称
admin.site.site_header = 'WebScanner 后台'
admin.site.site_title = 'WebScanner | 后台'


# 导航分类
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'icon_data','icon','get_items')
    list_display_links = ('id','name','icon_data','icon','get_items')
    search_fields = ('name',)
    ordering = ('sort','id',)

# 导航条目
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'desc','img_admin','img_width')
    list_display_links = ('id', 'title', 'img_admin','desc','img_width')
    list_filter = ('category',)
    search_fields = ('title','desc')

# 端口列表
@admin.register(PortList)
class PortListAdmin(admin.ModelAdmin):
    list_display = ('id', 'num','service', 'protocol','status')
    list_display_links = ('id', 'num','service', 'protocol','status')
    search_fields = ('num','service', 'protocol')
    list_per_page = 20