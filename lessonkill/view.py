from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello World")

from django.http import HttpResponse
import datetime
    
from django.shortcuts import render_to_response                               ## don't  forget to import

def index(request):
    position_index = "other links"
    return render_to_response('index.html', locals())

#def current_datetime(request):
#    now = datetime.datetime.now()
#    html = "<html><body>It is now %s.</body></html>" % now
#    return HttpResponse(html)

from django.template import Template, Context

def current_datetime(request):
    now = datetime.datetime.now()
        # one way to insert html
    # t = Template("<html><boby>It is now {{ current_date }}.</body></html>")
    # html = t.render(Context({'current_date': now}))
        # another way doesn't account for missing files
    #fp = open('../html/testtemplate.html')
    #t = Template(fp.read())
    #fp.close()
        # another way to get html
    #from django.template.loader import get_template
    #t = get_template('current_datetime.html')
    #html = t.render(Context({'current_date': now}))
    #return HttpResponse(html)
        #another way to return
    from django.shortcuts import render_to_response
    #return render_to_response('current_datetime.html', {'current_date': now})
        #using locals()
    current_date = datetime.datetime.now()
    return render_to_response('current_datetime.html', locals())
    

#fail to use class for render_to_response
class hours_Ahead(object):
    def __init__(self, off, ntime):
        self.next_time = ntime
        self.hour_offset = off

#def hours_ahead(request, template_name, hours_off): works too!!
def hours_ahead(request, hours_off, template_name):
    try:
        hour_offset = int(hours_off)
    except ValueError:
        raise Http404()
    next_time = datetime.datetime.now() + datetime.timedelta(hours = hour_offset)
    
    #one way to insert html
    #html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (hour_offset, next_time)
    #<p>In {{ hour_offset }} hour(s), it will be {{ next_time }}.<p>
    #return HttpResponse(html)

    from django.shortcuts import render_to_response                               ## don't  forget to import
#connet with html
    #return render_to_response('hours_ahead.html', locals())
    #return render_to_response('hours_ahead.html', {'hour_offset': hour_offset, 'next_time': next_time})

    #temp = []
    #temp.append(hour_offset)
    #temp.append(next_time)
    #temp = [hour_offset, next_time]
    temp = hours_Ahead(hour_offset, next_time)
    return render_to_response(template_name, {'temp': temp})
    #block can't work



def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    #for k, v in values:
    #    html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    #return HttpResponse('<table>%s</table>' % '\n'.join(html))

    return render_to_response('display_meta.html', {'html_values': values}) 

def display_request(request): # don't know type of below, have problem through html "BadHeaderError"
    request_path = request.path.rstrip()
    request_get_host = request.get_host().rstrip()
    request_get_full_path = request.get_full_path().rstrip()
    request_is_secure = request.is_secure()
    return HttpResponse('display_request.html', locals())

def requires_login(view):
    def new_view(request, *args, **kwargs):
        if not request.user.is_authenticated():
            return HttpResponseRedirect('/account/login/')
        return view(request, *args, **kwargs)
    return new_view

def my_view(request, month, day):
    return HttpResponse('display_request.html', locals())

## {link to another dirct or show html
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render_to_response

def some_page(request):
    if request.method == 'POST':
        #do_something_for_post()
        return  HttpResponseRedirect('/someurl')
    elif request.method == 'GET':
        #do_something_for_get()
        return render_to_response('page.html')
    else:
        raise Http404()


#def method_splitter(request, GET=None, POST=None):
#    if request.method == 'GET' and GET is not None:
#        return GET(request)
#    elif request.method == 'POST' and POST is not None:
#        return POST(request)
#    raise Http404
def method_splitter(request, *args, **kwargs):
    get_view = kwargs.pop('GET', None)
    post_view = kwargs.pop('POST', None) #default = None so it wouldn't have extra problems
    if request.method == 'GET' and get_view is not None:
        return get_view(request, *args, **kwargs)
    elif request.method == 'POST' and post_view is not None:
        return post_view(request, *args, **kwargs)
    raise Http404

def some_page_get(request):
    assert request.method == 'GET'
    do_something_for_get()
    return render_to_response('page.html')

def some_page_post(request):
    assert request.method == 'POST'
    do_something_for_post()
    return HttpResponseRedirect('/someurl/')

##} link to another dirct or show html

from django http import Http404
from django.template import TemplateDoesNotExist
from django.views.generic.simple import direct_to_template
##about_pages
def about_pages(request, page):
    try:
        return direct_to_template(request, template="about/%s.html" % page)
    except TemplateDoesNotExist:
        raise Http404()
                