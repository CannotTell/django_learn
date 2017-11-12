#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/9 下午2:58
# @Author  : JZK
# @File    : send_email.py
# @Software: PyCharm
# @Contact : eric.c.jzk@gmail.com
import string
import random
from users.models import EmailVerifyRecord
from django.core.mail import send_mail
from django_learn.settings import EMAIL_FROM
from django.contrib.sites.models import Site


def random_str(random_len=6):
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for _ in range(random_len))


def send_email(email, code_type='register'):

    email_record = EmailVerifyRecord()
    code = random_str(random_len=16)
    email_record.code = code
    email_record.email = email
    email_record.sendType = code_type
    email_record.save()

    email_title = ''
    email_body = ''

    if code_type == 'register':
        email_title = '激活链接'
        email_body = '请点击以下激活链接:http://{}/verifyCode/?type={}&code={}'.format(
                        Site.objects.get_current().domain, code_type, code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            print('sucess')