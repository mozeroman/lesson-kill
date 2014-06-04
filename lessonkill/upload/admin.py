from django.contrib import admin

# Register your models here.

from lessonkill.upload.models import Testupload

class TestuploadAdmin(admin.ModelAdmin):
    list_display = ('image', 'testfile')
    search_fields = ('image', 'testfile')


admin.site.register(Testupload, TestuploadAdmin)

