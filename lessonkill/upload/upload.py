#coding=utf-8

from django.shortcuts import render

# Create your views here.

from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response, render 
from django.template import RequestContext
from django.http import HttpResponseRedirect
from lessonkill.upload.forms import UploadFileForm
from lessonkill.upload.models import UserForm

@csrf_protect
def reg(request):

    if request.method == 'POST':#提交表单

        form = UserForm(request.POST,request.FILES)#如果表单中要传文件、图片，则需要传两个参数

        if form.is_valid():#这个is_valid通过model的配置定义，这里显现出blank=True的意义了

            form.save()#这一句save，不但保存了各个字段，而且自动将上传的文件保存到指定目录，并且生成文件路径，保存到user表的img字段中了。

    else:#显示表单

        form = UserForm()

    return render_to_response('reg_form.html', {'form': form}, context_instance=RequestContext(request))

@csrf_protect
def upload_index(request):
    """docstring for index"""
    return render(request, 'upload_index.html', {'title': 'test page'}, context_instance=RequestContext(request))

def upload(request):
    if request.method == 'POST':
        f = handle_uploaded_file(request.FILES['pic'])
        return render_to_response('upload.html', {'file':f})
    return render_to_response('upload.html', )

def handle_uploaded_file(hf):
    with open(hf.name, 'wb+') as info:
        for chunk in hf.chunks():
            info.write(chunk)
    return hf

def upload_file(request):
  if request.method == 'POST':
     form = UploadFileForm(request.POST, request.FILES)
     if form.is_valid():
        handle_uploaded_file2(request.FILES['file'])
        return HttpResponseRedirect('/../upload', )
  else:
     form = UploadFileForm()
  return render_to_response('upload_form.html', {'form': form})

def handle_uploaded_file2(f):
  destination = open('/media/habili.txt', 'wb+')
  for chunk in f.chunks():
    destination.write(chunk)
  destination.close()

