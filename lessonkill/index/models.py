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

class Teacher(models.Model):
    teacher_name = models.CharField('教师姓名', max_length = 30)
    teacher_introduction = models.TextField('教师简介', )
    teacher_website = models.URLField('教师主页', blank = True)
    teacher_image = models.ImageField('教师头像', upload_to='teacher', null=True, blank=True)

    teacher_release_time = models.DateTimeField('发布时间', auto_now = True, blank = True)

    def __unicode__(self):
        return u'%s' % (self.teacher_name, self.teacher_image)
 
