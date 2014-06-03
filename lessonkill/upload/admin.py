from django.contrib import admin

# Register your models here.

from lessonkill.upload.models import Testupload, User

class TestuploadAdmin(admin.ModelAdmin):
    list_display = ('image', 'testfile')
    search_fields = ('image', 'testfile')

class UserAdmin(admin.ModelAdmin):
    list_display = ('img', )
    search_fileds = ('name', )


admin.site.register(Testupload, TestuploadAdmin)
admin.site.register(User, UserAdmin)

