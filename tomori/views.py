from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required


def index(request):
    return render_to_response('index.html', context_instance=RequestContext(request))

@login_required
def mypage(request):
    return render_to_response('mypage.html', context_instance=RequestContext(request))