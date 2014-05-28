#coding=utf-8

####user

from django.http import HttpResponse
from django.shortcuts import render_to_response                               ## don't  forget to import
from django.template import RequestContext 

def index(request):
    position_index = "other links"
    return render_to_response('index.html', locals())

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







####chapter


