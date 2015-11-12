from django.shortcuts import render_to_response
from django.template import RequestContext

SITE_TITLE = 'django_test'

def index(request):
    return render_to_response('index.html', context_instance=RequestContext(request))
