#coding=utf-8

from django.http import HttpResponseRedirect

####user

from django.http import HttpResponse
from django.shortcuts import render_to_response                               ## don't  forget to import
from django.template import RequestContext 

def index(request):
    position_index = "other links"
    return render_to_response('index.html', locals())

def user_profile(request):
    return HttpResponseRedirect('/../../')

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

def register(request, template_name):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/books/")
    else:
        form = UserCreationForm()
    return render_to_response(template_name, {
        'form': form,
        })

from lessonkill.index.models import Mainindex
from lessonkill.chapter.models import Post

#auto load
##index/index
def autoload(request):
    try:
        tempmainindex = Mainindex.objects.get(class_name="LessonKill 软件工程")
    except Mainindex.DoesNotExist:
        tempmainindex = Mainindex()
        tempmainindex.class_name = "LessonKill 软件工程"
        tempmainindex.class_introduction = "软件工程是是以工程化的思想和方法来指导软件开发的整个过程的学科，具有鲜明的实践性。近年来在计算机和信息管理等领域中，它的地位显得越来越重要。不仅大型软件项目离不开它，就是一般的，甚至小型软件项目也必须运用它的概念、原则和方法。近年来，软件工程学科发生了巨大变化，从传统的结构化技术占主导地位，发展到面向对象技术占主导地位，继而发展到基于构件的技术成为开发技术主流。"
        tempmainindex.class_duration = '8-10小时/周'
        tempmainindex.class_outline = 'n章，m次测试，l次作业，获得软件工程师认证'
        tempmainindex.display_on_index = True
        tempmainindex.save()

##chapter/post
    try:
        temppost = Post.objects.get(post_title="第十二章")
    except:
        #from datetime import datetime
        temppost = Post()
        temppost.post_title = "Introduction to Software Engineering"
        temppost.post_chapter = "第一章"
        temppost.post_index = "Introduction to Software Engineering"
        temppost.save()
        temppost = Post()
        temppost.post_title = "Software Process"
        temppost.post_chapter = "第二章"
        temppost.post_index = "Software Process"
        temppost.save()
        temppost = Post()
        temppost.post_title = "Project Management"
        temppost.post_chapter = "第三章"
        temppost.post_index = "Project Management"
        temppost.save()
        temppost = Post()
        temppost.post_title = "System Analysis"
        temppost.post_chapter = "第四章"
        temppost.post_index = "System Analysis"
        temppost.save()
        temppost = Post()
        temppost.post_title = "Requirement Engineer"
        temppost.post_chapter = "第五章"
        temppost.post_index = "Requirement Engineer"
        temppost.save()
        temppost = Post()
        temppost.post_title = "Software Design"
        temppost.post_chapter = "第六章"
        temppost.post_index = "Software Design"
        temppost.save()
        temppost = Post()
        temppost.post_title = "User Interface Design"
        temppost.post_chapter = "第七章"
        temppost.post_index = "User Interface Design"
        temppost.save()
        temppost = Post()
        temppost.post_title = "Coding"
        temppost.post_chapter = "第八章"
        temppost.post_index = "Coding"
        temppost.save()
        temppost = Post()
        temppost.post_title = "Software Test"
        temppost.post_chapter = "第九章"
        temppost.post_index = "Software Test"
        temppost.save()
        temppost = Post()
        temppost.post_title = "Software Quality Management"
        temppost.post_chapter = "第十章"
        temppost.post_index = "Software Quality Management"
        temppost.save()
        temppost = Post()
        temppost.post_title = "Software Configuration Management"
        temppost.post_chapter = "第十一章"
        temppost.post_index = "Software Configuration Management"
        temppost.save()
        temppost = Post()
        temppost.post_title = "Software Maintainance"
        temppost.post_chapter = "第十二章"
        temppost.post_index = "Software Maintainance"
        temppost.save()


    return HttpResponseRedirect('/../')





