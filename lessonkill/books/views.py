from django.shortcuts import  render_to_response
from django.http import HttpResponse
from lessonkill.books.models import Book

# comments start only check input
#def search(request):
#    if 'q' in request.GET:
#        message = 'You searched for: %r' % request.GET['q']
#    else:
#        message = 'You submitted an empty form.'
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
    template_name = 'books/%s_list.html' % model.__name__.lower() #open books/account_list.html which doesn't exist
    return render_to_response(template_name, {'object_list': obj_list})

