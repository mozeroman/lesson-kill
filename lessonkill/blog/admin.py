from django.contrib import admin

# Register your models here.

from lessonkill.blog.models import BlogPost

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'timestamp')
    search_fields = ('title', 'body') # 'timestamp' is not a normal type

admin.site.register(BlogPost, BlogPostAdmin)

