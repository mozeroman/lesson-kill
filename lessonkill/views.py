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
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def register(request, template_name):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/../")
    else:
        form = UserCreationForm()
    return render_to_response(template_name, {
        'form': form,
        },context_instance=RequestContext(request))

from django.contrib.auth import authenticate, login as user_login, logout as user_logout # login 和 logout不能重复定义

@csrf_protect
def login(request, template_name):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/../')

    errors = []
    #tempusername = request.POST.get('username')
    #temppassword = request.POST.get('password')
    if request.method == 'POST':
        tempusername = request.POST.get('username')
        temppassword = request.POST.get('password')
        user = authenticate(username=tempusername, password=temppassword)
        if user is not None:
            if user.is_active:
                print 3
                user_login(request, user)
                print 4
                # Redirect to a success page.
                return HttpResponseRedirect("/../")
            else:
                errors.append('用户名未被授权')
                #login(request, user)
                # Return a 'disabled account' error message
                return render_to_response(template_name, {
                    'errors': errors,
                    } ,context_instance=RequestContext(request)
                    )
        else:
            errors.append('用户名或密码错误')

    return render_to_response(template_name, {
        'errors': errors,
        } ,context_instance=RequestContext(request)
        )
    # Return an 'invalid login' error message.

def logout(request):
    user_logout(request)
    return HttpResponseRedirect("/../")
    # Return an 'invalid login' error message.

from lessonkill.index.models import Mainindex, Teacher
from lessonkill.chapter.models import Post

#auto load
##index/index
def autoload(request):

    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')

    try:
        tempteacher = Teacher.objects.get(teacher_name="韩智")
    except Teacher.DoesNotExist:
        tempteacher = Teacher()
        tempteacher.teacher_name = "韩智"
        tempteacher.teacher_introduction = "南开大学软件学院 副教授 博士生导师 研究方向：生物信息、图像处理、模式识别、软件工程教授课程：《软件工程》《数字图像处理》《基于CDIO理念的软件工程课程教学改革与实践》"
        tempteacher.teacher_website = 'http://www.nankai.edu.cn'
        tempteacher.teacher_image = "/static/css/images/avatar.png"
        tempteacher.save()

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


def autodelete(request):

    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')

    try:
        Teacher.objects.filter(teacher_name="韩智").delete()
    except Teacher.DoesNotExist:
        pass

    try:
        Mainindex.objects.filter(class_name="LessonKill 软件工程").delete()
    except Mainindex.DoesNotExist:
        pass

##chapter/post
    try:
       Post.objects.filter(post_chapter="第一章").delete()
       Post.objects.filter(post_chapter="第二章").delete()
       Post.objects.filter(post_chapter="第三章").delete()
       Post.objects.filter(post_chapter="第四章").delete()
       Post.objects.filter(post_chapter="第五章").delete()
       Post.objects.filter(post_chapter="第六章").delete()
       Post.objects.filter(post_chapter="第七章").delete()
       Post.objects.filter(post_chapter="第八章").delete()
       Post.objects.filter(post_chapter="第九章").delete()
       Post.objects.filter(post_chapter="第十章").delete()
       Post.objects.filter(post_chapter="第十一章").delete()
       Post.objects.filter(post_chapter="第十二章").delete()
    except:
        pass


    return HttpResponseRedirect('/../')



