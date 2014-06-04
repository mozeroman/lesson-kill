#coding=utf-8

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect

from django.http import HttpResponse
from django.shortcuts import render_to_response                               ## don't  forget  to import
from django.template import RequestContext 
from lessonkill.index.models import Mainindex, Teacher
from lessonkill.chapter.models import Post
#from django.contrib.auth import user

def index(request):

    if request.user.is_authenticated():
        position_index = "课程介绍"
    else:
        position_index = '课程介绍'

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

    try:
        teachers = Teacher.objects.all()
    except Teacher.DoesNotExist:
        pass

    student_count = 0;
    stu_finish_count = 0;
    stu_cerf_count = 0;
    teacher_count = 1;
    social_count = 0;


    return render_to_response('index.html', locals(), context_instance=RequestContext(request))

#def index_redirect(request):
#    return HttpResponseRedirect('')

