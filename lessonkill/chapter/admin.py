#coding=utf-8
from django.contrib import admin

# Register your models here.

from lessonkill.chapter.models import Posts

class PostsAdmin(admin.ModelAdmin):
    list_display = ('post_type', 'post_date', 'post_deadline')
    search_field = ('post_index')


admin.site.register(Posts, PostsAdmin)
