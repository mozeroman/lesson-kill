from django.shortcuts import render_to_response
from django.http import HttpResponse
from lessonkill.blog.models import BlogPost

# Create your views here.

def blog(request, template_name):
    posts = BlogPost.objects.all()
    return render_to_response(template_name, {'posts' : posts})
    
