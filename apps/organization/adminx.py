#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/14 下午3:01
# @Author  : JZK
# @File    : adminx.py
# @Software: PyCharm
# @Contact : eric.c.jzk@gmail.com

import xadmin
from .models import CityDict, CourseOrg, Teacher


class CityDictAdmin(object):
    list_display = ['name', 'desc', 'addTime']
    search_fields = ['name', 'desc', 'addTime']
    list_filter = ['name', 'desc', 'addTime']


class CourseOrgAdmin(object):
    list_display = ['name', 'desc', 'category', 'clickNum', 'favNum', 'image', 'address', 'addTime', 'city']
    search_fields = ['name', 'desc', 'category', 'clickNum', 'favNum', 'image', 'address', 'addTime', 'city']
    list_filter = ['name', 'desc', 'category', 'clickNum', 'favNum', 'image', 'address', 'addTime', 'city']


class TeacherAdmin(object):
    list_display = ['name', 'workYear', 'Company', 'workTitle', 'clickNum', 'favNum', 'addTime', 'org']
    search_fields = ['name', 'workYear', 'Company', 'workTitle', 'clickNum', 'favNum', 'addTime', 'org']
    list_filter = ['name', 'workYear', 'Company', 'workTitle', 'clickNum', 'favNum', 'addTime', 'org']


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)