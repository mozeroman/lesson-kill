from django.conf.urls import patterns, include, url
from lessonkill import view
from lessonkill.books import views, search
#from coursekill.contact.views import  contact
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    ## js, css, pics, import
    url( r'^static/(?P<path>.*)$', 'django.views.static.serve', { 'document_root':settings.STATIC_ROOT }),
    # Examples:
    # url(r'^$', 'lessonkill.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', view.index),
    url(r'hello/$', view.hello),
    url(r'time/$', view.current_datetime),
    url(r'time/plus/(\d{1,2})/$', view.hours_ahead),
    url(r'meta/$', view.display_meta),
    url(r'request/$', view.display_request),
    url(r'search/$', views.search),
    url(r'search_account/$', search.search_account),
    url(r'contact/$', 'lessonkill.contact.views.contact'),
    url(r'^admin/', include(admin.site.urls)),
)
