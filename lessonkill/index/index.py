#coding=utf-8

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect

from django.http import HttpResponse
from django.shortcuts import render_to_response                               ## don't  forget  to import
from django.template import RequestContext 

def index(request):
    position_index = "课程概况"
    class_name = "LessonKill 软件工程"
    return render_to_response('index.html', locals(), context_instance=RequestContext(request))

#def index_redirect(request):
#    return HttpResponseRedirect('')

