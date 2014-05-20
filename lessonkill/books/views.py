from django.shortcuts import  render_to_response
from django.http import HttpResponse
from lessonkill.books.models import Book

# comments start only check input
#def search(request):
#    if 'q' in request.GET:
#        message = 'You searched for: %r' % request.GET['q']
#    else: #        message = 'You submitted an empty form.'
#    return HttpResponse(message)
# comments end

def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.') 
        else:
            books = Book.objects.filter(title__icontains = q)
            return render_to_response('search_result.html', {'books': books, 'query': q})

    return render_to_response('search_form.html', {'errors': errors})

def object_list(request, model):
    obj_list = model.objects.all()
    template_name = '%s_list.html' % model.__name__.lower() #open books/account_list.html which doesn't exist
    return render_to_response(template_name, {'object_list': obj_list})

from django.db import connection

def account_list(request):
    db = MySQLdb.connect(user='root', db='django.db.backends.mysql', passwd='1112611', host='localhost')
    cursor = connetion.cursor()
    cursor.execute('SELECT name FROM accounts ORDER BY name')
    object_list = [row[0] for row in cursor.fetchall()]
    db.close()
    return render_to_response('account_list.html', {'object_list': object_list})

import datetime
from django.shortcuts import get_object_or_404
#from django.views.generic import list_detail
from lessonkill.books.models import Author

#def author_detail(request, author_id):
    # Delegate to the generic view and get an HttpResponse.
#    response = list_detail.object_detail(
#        request,
#        queryset = Author.objects.all(),
#        object_id = author_id,
#    )

    # Record the last accessed date. We do this *after* the call
    # to object_detail(), not before it, so that this won't be called
    # unless the Author actually exists. (If the author doesn't exist,
    # object_detail() will raise Http404, and we won't reach this point.)
#    now = datetime.datetime.now()
#    Author.objects.filter(id=author_id).update(last_accessed=now)

#    return response

def author_list_plaintext(request):
    response = list_detail.object_list(
            request,
            queryset = Author.objects.all(),
            mimetype = 'text/plain',
            template_name = 'books/author_list.txt'
            )
    response["Content-Disposition"] = "attachment; filename=authors.txt" #tell web-browser to download this page instead giving a view
    return response

