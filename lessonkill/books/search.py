from django.shortcuts import  render_to_response
from django.http import HttpResponse, HttpResponseRedirect
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

def account_register(request, template_name):
    account = Account()
    errors = []
    if request.method == 'POST':
        if 'name' in request.POST:
            account.username = request.GET['name']
            try:
                p = Account.objects.get(username=account.username)
                errors.append('Username already exist')
            except Publisher.DoesNotExist:
                pass

        if 'psw' in request.POST:
            psw = request.GET['psw']
        else:
            errors.append('Password should not be empty')

        if 'psw_comfirm' in request.POST:
            psw_comfirm = request.GET['psw']
            if psw_comfirm != psw:
                errors.append('Password not match')
        else:
            errors.append('Password not match')

        if errors:
            return render_to_response(template_name, {
                'errors' : errors,
                #'name' : account.username, 
                #'psw' : '',
                #'psw_comfirm' : '', 
                #'signature' : account.signature,
                })
        else:
            account.save()
            return HttpResponseRedirect("/accounts/")
    else:
        return render_to_response(template_name, {
            'errors' : errors,
            })
        #Publisher.objects.filter(country='USA').delete() ##for delete

#p1 = Publisher(name='Apress', address='2855 Telegraph Avenue',
#...     city='Berkeley', state_province='CA', country='U.S.A.',
#...     website='http://www.apress.com/')
#>>> p1.save()

