#coding=utf-8
from django.db import models
from datetime import datetime

# Create your models here.

class Post(models.Model):
    POSTS_TYPE = (
            (u'announce',u'通知'),
            (u'chapter',u'课程'),
            (u'homework',u'作业'),
            )

    post_type = models.CharField('展出类型', max_length = 30, choices = POSTS_TYPE, default = u'chapter')
    post_title = models.CharField('标题', max_length = 50)
    post_chapter = models.CharField('章节', blank = True, max_length = 10)
    post_index = models.TextField('内容', )
    post_date = models.DateTimeField('发布时间', auto_now = True, blank = True)
    post_deadline = models.DateTimeField('截止日期', default = datetime.now, ) ### 不明原因不能为空
    post_ppt = models.FileField('附件', upload_to=post_type, blank=True)
    post_video = models.FileField('附件', upload_to=post_type, blank=True)

    class Meta:
        ordering = ['post_chapter']
        #ordering = []

    def __unicode__(self):
        return u'%s %s %s' % (self.post_type, self.post_title, self.post_date)
