#coding=utf-8
from django.db import models
from datetime import datetime

# Create your models here.

class Posts(models.Model):
    POSTS_TYPE = (
            (u'announce',u'通知'),
            (u'chapter',u'课程'),
            (u'homework',u'作业'),
            )

    post_type = models.CharField('展出类型', max_length = 30, choices = POSTS_TYPE)
    post_index = models.TextField('内容', )
    post_date = models.DateTimeField('发布时间', auto_now = True)
    post_deadline = models.DateTimeField('截止日期', )

    class Meta:
        ordering = ['-post_deadline']

    def __unicode__(self):
        return u'%s %s' % (self.post_type, self.post_date)
