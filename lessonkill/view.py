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

from django.http import Http404
from django.template import TemplateDoesNotExist
#from django.views.generic.simple import direct_to_template
#from django.views.generic.simple import direct_to_template
##about_pages
def about_pages(request, page):
    try:
#        return direct_to_template(request, template="about/%s.html" % page)
        return HttpResponse("direct_to_template is missing")
    except TemplateDoesNotExist:
        raise Http404()
                
def post_comment(request):
    if request.method != 'POST':
        raise Http404('Only POSTs are allowed')

    if 'comment' not in request.POST:
        raise Http404('Comment not submitted')

    c = comments.Comment(comment = request.POST['comment'])
    c.save()
    request.session['has_commented'] = True
    return HttpResponse('Thanks for your comment!')

def login(request):
    if request.method != 'POST':
        raise Http404('Only POSTs are allowed')
        #request.session.set_test_cookie()
        #return render_to_response('login.html')
    try:
        if request.session.test_cookie_worked(): 
            request.session.delete_test_cookie()

            m = Member.objects.get(username = request.POST['username'])
            if m.password == request.POST['password']:
                request.session['member_id'] = m.id
                return HttpResponseRedirect('/you-are-logged-in')
        else:
            return HttpResponse("Please enable cookies and try again.")
    except Member.DoesNotExist:
        return HttpResponse("Your username and password didn't match.")

def logout(request):
    try:
        del request.session['member_id']
    except KeyError:
        pass
    return HttpResponse("You're logged out.")

from django.contrib import auth

def login_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username = username, password = password)
    if user is not None and user.is_active:
        auth.login(request, user)       #Correct password, and the user is marked "active"
        return HttpResponseRedirect("/account/loggedin/") #Redirect to a success page.
    else:
        return HttpResponseRedirect("/account/invalid") #Show an error page

def logout_view(request):
    auth.logout(request)
    return HttpResponseRedirect("/account/loggedout/") #Redirect to a success page.

def my_view1(request):       #login example
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)
    # ...
    return HttpResponse("this is an example for login view")

from django.contriv.auth.decorators import login_required

@login_required
def my_view2(request):
    # ...
    return HttpResponse("this is another example for login view")

def vote(request):
    if request.user.is_authenticated() and request.user.has_perm('polls.can_vote'):
        # vote here
    else:
        return HttpResponse("You can't vote in this poll.")

def user_can_vote(user):
    return user.is_authenticated() and user.has_perm("polls.can_vote")

@user_passes_test(user_can_vote, login_url="/login/")
def vote1(request):
    #Code here can assume a logged-in user with the corrent permission
    #...
    return HttpResponse("Thank you for your vote.")
#also work as:

from django.contrib.auth.decorators import permission_required

@permission_required('polls.can_vote', login_url="/login/")
def vote2(request):
    #Code here can assume a logged-in user with the corrent permission
    #...
    return HttpResponse("Thank you for your vote.")

from django.contrib.auth.decorators import login_required
from django.views.generic.date_based import object_detail

@login_required
def limited_object_detail(*args, **kwargs):
    return object_detail(*args, **kwargs)

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

def register(request, template_name):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/books/")
    else:
        form = UserCreationForm()
    return render_to_response(template_name, {
        'form': form,
        })

def create_playlist(request, songs):
    request.user.message_set.create(
            message = "Your playlist was added successfully."
            )
    return render_to_response("playlists/create.html",
            context_instance = RequestContextt(request))

