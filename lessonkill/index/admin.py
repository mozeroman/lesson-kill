from django.contrib import admin

# Register your models here.

from lessonkill.index.models import Mainindex, Teacher

class MainindexAdmin(admin.ModelAdmin):
    list_display = ('class_name', 'display_on_index')
    search_fields = ('class_name', 'class_introduction')

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('teacher_name', 'teacher_release_time')
    search_fields = ('teacher_name', 'teacher_introdection')


admin.site.register(Mainindex, MainindexAdmin)
admin.site.register(Teacher, TeacherAdmin)
