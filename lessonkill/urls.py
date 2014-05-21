from django.contrib.auth.views import login, logout # professional login logout

from django.conf.urls import patterns, include, url
from lessonkill import view
from lessonkill.books import views, search, models
from lessonkill.blog.views import blog
#from coursekill.contact.views import  contact
from  django.conf import settings

from django.contrib import admin
admin.autodiscover()

#from django.conf.urls. import *
# generic is missing
#from django.views.generic.simple import direct_to_template



urlpatterns = patterns('',
    url(r'^$', view.index),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:

    #from django.views.generic import list_detail
    from lessonkill.books.models import Publisher, Book

    def get_books():
        return Book.objects.all()

    publisher_info = {
            'queryset': Publisher.objects.all(),
            'template_name': 'publisher_list.html',
            'template_object_name': 'publisher', #create a var name
            'extra_context': {'book_list': get_books} #need def get_books()
            #'extra_context': {'book_list': Book.objects.all} # do the same
            }

    book_info = {
            'querset': Book.objects.order_by('-publication_date'),
            }
    apress_books = {
            'querset': Book.objects.filter(publisher__name='Apress Publishin'),
            'template_name': 'books/apress_list.html',
            }

    from django.shortcuts import get_object_or_404
    #from django.views.generic import list_detail
    from lessonkill.books.models import Book, Publisher

    def books_by_publisher(request, name):
        # Look up the publisher (and raise a 404 if it can't be found).
        publisher = get_object_or_404(Publisher, name__iexact=name)

        # Use the object_list view for the heavy lifting.
        return list_detail.object_list(
                request,
                queryset = Book.objects.filter(publisher=publisher),
                template_name = 'books/books_by_publisher.html',
                template_object_name = 'book',
                extra_context = {'publisher': publisher}
                )

   # from lessonkill.books.views import author_detail, author_list_plaintext
    urlpatterns += patterns('',
          #  url(r'^publishers/$', list_detail.object_list, publisher_info), #publisher_info define above
          #  url(r'^books/$', list_detail.object_list, book_info),
          #  url(r'^books/apress/$', list_detail.object_list, apress_books),

            url(r'^book/(\w+)/$', books_by_publisher),

          #  url(r'^authors/(?P<author_id>\d+)/$', author_detail),
          #  url(r'^authors/plain/$', author_list_plaintext),

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
            url(r'contact/$', 'lessonkill.contact.views.contact'),

            url(r'mydata/birthday/$', view.my_view, {'month': 'apr', 'day': '09'}),
            url(r'mydata/(?P<month>\w{3})/(?P<day>\d\d)/$', view.my_view),
            url(r'^view1/$', view.requires_login(view.my_view)),
            url(r'^view2/$', view.requires_login(view.my_view)),

            url(r'^publisher/$', views.object_list, {'model': models.Publisher}), #import books.model and books. views
            url(r'^accounts/$', views.object_list, {'model': models.Account}), #import books.model and books. views
            url(r'^search_account/$', search.search_account),       #Opencourse works

            url(r'^somepage/$', view.some_page),
            url(r'^somepage2/$', view.method_splitter, {'GET': view.some_page_get, 'POST': view.some_page_post}),

            # url(r'^about/$', view.direct_to_template, {'template', 'about.html'}),
            # url(r'^about/(\w+)/$', about_pages),

            url(r'^accounts/login/$', login, {'template_name': 'login.html_template'}),
            url(r'^accounts/logout/$', logout, {'template_name': 'logout.html'}),

            url(r'^register/$', view.register, {'template_name': 'register.html_template'}),
            url(r'^account_register/$', search.account_register, {'template_name': 'account_register.html'}),
            
            url(r'^blog/$', blog, {'template_name': 'blog.html'}),
            )
