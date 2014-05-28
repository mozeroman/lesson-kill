from django.contrib import admin

# Register your models here.

from lessonkill.index.models import Mainindex

class MainindexAdmin(admin.ModelAdmin):
    list_display = ('class_name', 'display_on_index')
    search_fields = ('class_name', 'class_introduction')


admin.site.register(Mainindex, MainindexAdmin)
