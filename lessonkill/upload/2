#coding=utf-8

from django.db import models

# Create your models here.

class Testupload(models.Model):
    image = models.ImageField('介绍图片', upload_to='up', null=True, blank=True)
    testfile = models.FileField('测试上传文件', upload_to='./')

    #def __unicode__(self):
    #    return u'%s %s' % (self.image, self.testfile)

