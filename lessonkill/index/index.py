#coding=utf-8

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect

from django.http import HttpResponse
from django.shortcuts import render_to_response                               ## don't  forget  to import
from django.template import RequestContext 
from lessonkill.index.models import Mainindex
from lessonkill.chapter.models import Post

def index(request):

    position_index = "课程概况"

    try:
        mainindex = Mainindex.objects.get(display_on_index = True)
        class_name = mainindex.class_name
        class_introduction = mainindex.class_introduction
        class_duration = mainindex.class_duration
        class_outline = mainindex.class_outline
    except Mainindex.DoesNotExist:
        pass

    try:
        chapters = Post.objects.filter(post_type = u'chapter')
    except Post.DoesNotExist:
        pass

    student_count = 10;
    stu_finish_count = 9;
    stu_cerf_count = 8;
    teacher_count = 1;
    social_count = 0;
    teacher_name = "韩智"
    teacher_introduction = "南开大学软件学院 副教授 博士生导师 研究方向：生物信息、图像处理、模式识别、软件工程教授课程：《软件工程》《数字图像处理》《基于CDIO理念的软件工程课程教学改革与实践》"
    teacher_release_time = "04/20/2014"
    teacher_website = 'http://www.nankai.edu.cn'
    return render_to_response('index.html', locals(), context_instance=RequestContext(request))

#def index_redirect(request):
#    return HttpResponseRedirect('')

