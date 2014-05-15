from django.conf.urls import patterns, include, url
from lessonkill import view
from lessonkill.books import views, search, models
#from coursekill.contact.views import  contact
from  django.conf import settings

from django.contrib import admin
admin.autodiscover()

#from django.conf.urls. import *



urlpatterns = patterns('',
    url(r'^$', view.index),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:

    urlpatterns += patterns('',
            url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_PATH, 'show_indexes':True}),  
            ## js, css, pics, import
            #url( r'^html/(?P<path>.*)$', 'django.views.static.serve', { 'document_root':settings.STATIC_ROOT }),
            #url(r'^css/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.CSS_ROOT }),
            #url(r'^js/(?P</path><path>.*)$', 'django.views.static.serve', {'document_root': settings.JS_ROOT }),
            #url(r'^images/(?P</path><path>.*)$', 'django.views.static.serve', {'document_root': settings.IMAGES_ROOT }),
            #url(r'^images/(?P</path><path>.*)$', 'django.views.static.serve', {'document_root': '/home/namor/codes/lesson-kill/html/css/images'}),

            # Examples:
            # url(r'^$', 'lessonkill.views.home', name='home'),
            # url(r'^blog/', include('blog.urls')),

            url(r'hello/$', view.hello),
            url(r'time/$', view.current_datetime),
            url(r'time/plus/(?P<hours_off>\d{1,2})/$', view.hours_ahead, {'template_name': 'hours_ahead.html'}),
            url(r'meta/$', view.display_meta),
            url(r'request/$', view.display_request),
            url(r'search/$', views.search),
            url(r'search_account/$', search.search_account),
            url(r'contact/$', 'lessonkill.contact.views.contact'),

            url(r'mydata/birthday/$', view.my_view, {'month': 'apr', 'day': '09'}),
            url(r'mydata/(?P<month>\w{3})/(?P<day>\d\d)/$', view.my_view),
            url(r'^view1/$', view.requires_login(view.my_view)),
            url(r'^view2/$', view.requires_login(view.my_view)),

            url(r'^publisher/$', views.object_list, {'model': models.Publisher}), #import books.model and books. views
            url(r'^accounts/$', views.object_list, {'model': models.Account}), #import books.model and books. views

            url(r'^somepage/$', view.some_page),
            url(r'^somepage2/$', view.method_splitter, {'GET': view.some_page_get, 'POST': view.some_page_post}),
            )
