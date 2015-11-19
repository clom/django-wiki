from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from tomori.forms import *


def menu(request):
    art = Article.objects.all().order_by('id')
    return render_to_response('menu.html', {'article': art}, context_instance=RequestContext(request))


def index(request):
    return render_to_response('index.html', context_instance=RequestContext(request))


@login_required
def mypage(request):
    return render_to_response('mypage.html', context_instance=RequestContext(request))


def a_read(request, article_id):
    text = Article.objects.get(pk=article_id)
    return render_to_response('view.html', {'text': text}, context_instance=RequestContext(request))


def add(request, article_id=None):
    if article_id:
        article = get_object_or_404(Article, pk=article_id)
    else:
        article = Article()

    if request.method == 'POST':
        form = FormArticle(request.POST, instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            article.username = request.user
        article.save()
        return redirect('/pages/' + article.id.__str__())
    else:
        form = FormArticle(instance=article)
        return render_to_response('new.html', dict(form=form, article_id=article_id),
                                  context_instance=RequestContext(request))

def delete(request):
    return render_to_response('mypage.html', context_instance=RequestContext(request))
