#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/9 上午11:34
# @Author  : JZK
# @File    : forms.py
# @Software: PyCharm
# @Contact : eric.c.jzk@gmail.com

from django import forms
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)
    captcha = CaptchaField(error_messages={'invalid': '验证码错误'})


class ForgetPwdForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={'invalid': '验证码错误'})
