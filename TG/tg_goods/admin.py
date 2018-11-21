from __future__ import unicode_literals
from tg_goods.models import GoodsInfo,TypeInfo
from django.contrib import admin

class TypeInfoAdmin(admin.ModelAdmin):
    list_display = ['id','ttitle']


class GoodsInfoAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ['id', 'gtitle', 'gprice', 'gunit', 'gkucun', 'gcontent', 'gtype']


admin.site.register(TypeInfo,TypeInfoAdmin)
admin.site.register(GoodsInfo,GoodsInfoAdmin)