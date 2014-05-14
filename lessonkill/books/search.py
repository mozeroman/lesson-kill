from django.shortcuts import  render_to_response
from django.http import HttpResponse
from lessonkill.books.models import Account

# comments start only check input
#def search(request):
#    if 'q' in request.GET:
#        message = 'You searched for: %r' % request.GET['q']
#    else:
#        message = 'You submitted an empty form.'
#    return HttpResponse(message)
# comments end

def search_account(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.') 
        else:
            accounts = Account.objects.filter(username__icontains = q)
            return render_to_response('search_account.html', {'accounts': accounts, 'query': q})

    return render_to_response('search_account.html', {'errors': errors})

