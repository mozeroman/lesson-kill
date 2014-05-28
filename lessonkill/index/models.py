#coding=utf-8

from django.db import models
from datetime import datetime

# Create your models here.

class Mainindex(models.Model):
    class_name = models.CharField('课程名称', max_length = 30)
    class_introduction = models.TextField('课程简介')
    class_duration = models.CharField('课时', max_length = 20)
    class_outline = models.CharField('学习量', max_length = 50)
    display_on_index = models.BooleanField('是否显示在主页上', unique = True)

    def __unicode__(self):
        return u'%s %s' % (self.class_name, self.display_on_index)



