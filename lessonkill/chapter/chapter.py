#coding=utf-8
# chapter

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect

from django.http import HttpResponse
from django.shortcuts import render_to_response                               ## don't  forget to import
from django.template import RequestContext 

def chapter_study(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    return render_to_response('chapter-study.html', locals(), context_instance=RequestContext(request))

def chapter_study_num(request, chapter_number):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    return render_to_response('chapter-study.html', locals(), context_instance=RequestContext(request))

def chapter_practise(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    return render_to_response('chapter-practise.html', locals(), context_instance=RequestContext(request))

def chapter_test(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    return render_to_response('chapter-test.html', locals(), context_instance=RequestContext(request))

def chapter_discuss(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    return render_to_response('chapter-discuss.html', locals(), context_instance=RequestContext(request))


