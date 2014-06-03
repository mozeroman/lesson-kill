#coding=utf-8

from django.db import models

# Create your models here.

class Testupload(models.Model):
    image = models.ImageField('介绍图片', upload_to='up', null=True, blank=True)
    testfile = models.FileField('测试上传文件', upload_to='./')

    #def __unicode__(self):
    #    return u'%s %s' % (self.image, self.testfile)


class User(models.Model):

    GENDER_CHOICE = (
            (u'M', u'Male'),
            (u'F', u'Female'),
            )

    name = models.CharField(max_length=30)

    password = models.CharField(max_length=30)

    gender = models.CharField(max_length=2,choices = GENDER_CHOICE)

    birthday = models.DateField(null=True)

    img = models.ImageField(upload_to='/up',null=True,blank=True)

    phoneNum = models.CharField(max_length=13,null=True,blank=True)

    email = models.EmailField(null=True,blank=True)

    hobbies = models.CharField(max_length=100,null=True,blank=True)

    regTime = models.DateTimeField(null=True,blank=True)

    bio = models.TextField(null = True,blank=True)

    def __unicode__(self):

        return self.name

# in myapp1/models.py

from django.forms import ModelForm

from django import forms

class UserForm(ModelForm):

    class Meta:

        model = User #通过上面的User Model生成表单

        exclude =('regTime', )#将regTime字段排除在外

        widgets = {

            'password':forms.PasswordInput(),#将password字段的input type设为password

        }

