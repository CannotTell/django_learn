#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/15 下午6:30
# @Author  : JZK
# @File    : forms.py
# @Software: PyCharm
# @Contact : eric.c.jzk@gmail.com
from django import forms
from .models import UserAsk


class UserAskForm(forms.ModelForm):

    class Meta:
        model = UserAsk
        fields = ['name', 'mobile', 'courseName']