from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello World")

from django.http import HttpResponse
import datetime
    
from django.shortcuts import render_to_response                               ## don't  forget to import


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

def hours_ahead(request, offset):
    try:
        hour_offset = int(offset)
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
    return render_to_response('hours_ahead.html', {'temp': temp})
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

