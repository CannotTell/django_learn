# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-06 12:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0002_auto_20171102_1358'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usermessage',
            options={'verbose_name': '用户留言信息', 'verbose_name_plural': '用户留言信息'},
        ),
    ]
