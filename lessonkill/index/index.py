#coding=utf-8

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect

from django.http import HttpResponse
from django.shortcuts import render_to_response                               ## don't  forget  to import
from django.template import RequestContext 
from lessonkill.index.models import Mainindex

def index(request):

    position_index = "课程概况"

    mainindex = Mainindex.objects.get(display_on_index = True)
    class_name = mainindex.class_name
    class_introduction = mainindex.class_introduction
    class_duration = mainindex.class_duration
    class_outline = mainindex.class_outline

    student_count = 10;
    stu_finish_count = 9;
    stu_cerf_count = 8;
    teacher_count = 1;
    social_count = 0;
    teacher_site = 'http://www.nankai.edu.cn'
    return render_to_response('index.html', locals(), context_instance=RequestContext(request))

#def index_redirect(request):
#    return HttpResponseRedirect('')

