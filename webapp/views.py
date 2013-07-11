# Create your views here.
# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import datetime
from webapp.models import *
from webapp.forms import *
from django.template import Context, loader
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login

def hello(request):
    return HttpResponse("Hello world")

def search_form(request):
    return render_to_response('search_form.html')

def search(request):
    if 'q' in request.GET:
        message = 'You searched for: %r' % request.GET['q']
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def register_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
        return HttpResponseRedirect('/webapp/')
    else:
        form = RegistrationForm()
        variables = RequestContext(request, {'form': form})
        return render_to_response ('register.html',variables)

def login_user(request):
    state = "Please log in below..."
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You're successfully logged in!"
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."
    return render_to_response('login.html',
                                {'state':state,'username': username},
                                context_instance=RequestContext(request))

def show_product(request, product_id):
    product_id = int(product_id)
    product = Product_Primary_Table.objects.filter(id=product_id)
    product_info = product[0].product_information_table_set.all()
    pics = product[0].product_pic_table_set.all()
    return render_to_response("product.html", {'product': product[0], 
                                               'product_info': product_info,
                                               'pics':pics})

def square_product(request):
    product = Product_Primary_Table.objects.all()

