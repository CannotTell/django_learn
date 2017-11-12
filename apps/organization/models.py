# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class CityDict(models.Model):
    name = models.CharField(max_length=20, verbose_name='城市')
    desc = models.CharField(max_length=200, verbose_name='描述')
    addTime = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '城市'
        verbose_name_plural = verbose_name

class CourseOrg(models.Model):
    name = models.CharField(max_length=50, verbose_name='机构名称')
    desc = models.TextField(verbose_name = '机构描述')
    clickNum = models.IntegerField(default=0, verbose_name='点击数')
    favNum = models.IntegerField(default=0, verbose_name='收藏数')
    image = models.ImageField(upload_to='org/%Y/%M', verbose_name='封面')
    address = models.CharField(max_length=150, verbose_name=u'所在城市')
    addTime = models.DateTimeField(auto_now_add=True)
    city = models.ForeignKey(CityDict, verbose_name='所在城市')

    class Meta:
        verbose_name = '课程机构'
        verbose_name_plural = verbose_name


class Teacher(models.Model):
    name = models.CharField(max_length=50, verbose_name='教师名称')
    workYear = models.IntegerField(default=0,verbose_name='工作年限')
    Company = models.CharField(max_length=20, verbose_name='公司')
    workTitle = models.CharField(max_length=50, verbose_name=u'公司职位')
    clickNum = models.IntegerField(default=0, verbose_name='点击数')
    favNum = models.IntegerField(default=0, verbose_name='收藏数')
    addTime = models.DateTimeField(auto_now_add=True)
    org = models.ForeignKey(CourseOrg, verbose_name='所属机构')

    class Meta:
        verbose_name = '教师'
        verbose_name_plural = verbose_name