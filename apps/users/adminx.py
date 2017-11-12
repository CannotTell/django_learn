#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/8 下午1:04
# @Author  : JZK
# @File    : adminx.py
# @Software: PyCharm
# @Contact : eric.c.jzk@gmail.com
import xadmin
from xadmin import views
from .models import EmailVerifyRecord, Banner


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True

class GlobalSettings(object):
    site_title = 'xxx后台管理系统'
    site_footer = 'xx网'
    menu_style = 'accordion'

class EmailVerifyRecordAdmin(object):
    list_display = ['email', 'sendType', 'code', 'sendTime']
    search_fields = ['email', 'sendType', 'code', ]
    list_filter = ['email', 'sendType', 'code', 'sendTime']

class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'addTime']
    search_fields = ['title', 'image', 'url', 'index' ]
    list_filter = ['title', 'image', 'url', 'index', 'addTime']

xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)