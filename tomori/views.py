from django.shortcuts import render_to_response
from django.template import RequestContext
from tomori.forms import *


def index(request):
    return render_to_response('index.html', context_instance=RequestContext(request))


def login(request):
    f = LoginForm()
    return render_to_response('login.html', {'SIGN_IN': f}, context_instance=RequestContext(request))
