from django.http.response import HttpResponse, Http404
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response, redirect, render
from article.models import Article, Comments
from django.core.exceptions import ObjectDoesNotExist
from forms import CommentForm
from django.core.context_processors import csrf
from django.core.paginator import Paginator
from django.contrib import auth

from polls.models import Choice, Question

from django.contrib.auth.models import User
from datetime import datetime

def index(request):
    return redirect('/page/1/')


def about(request):
    return render(request, 'about.html', {'username': auth.get_user(request).username})

def articles(request, page_number=1):

    question = Question.objects.get(pk=2)

    all_articles = Article.objects.all().order_by('-id')
    current_page = Paginator(all_articles, 3)
    current_page2 = Paginator(all_articles, 100)
    return render_to_response(
        'articles.html',
        {'articles': current_page.page(page_number),
         'articles2': current_page2.page(1),
         'username': auth.get_user(request).username,


        'question': question,
        'articles':current_page.page(page_number)})

def article(request, article_id=1):
    comment_form = CommentForm
    args = {}
    args.update(csrf(request))
    args['article'] = Article.objects.get(id=article_id)
    args['comments'] = Comments.objects.filter(comments_article_id=article_id)
    args['form'] = comment_form
    args['username'] = auth.get_user(request).username
    return render_to_response('article.html', args)

def addlike(request, article_id):
    back_url = request.META.get('HTTP_REFERER','/')
    try:
        if article_id in request.COOKIES:
            redirect(back_url)
        else:
            article = Article.objects.get(id=article_id)
            article.article_likes += 1
            article.save()
            response = redirect(back_url)
            response.set_cookie(article_id, "test")
            return response
    except ObjectDoesNotExist:
        raise Http404
    return redirect(back_url)


def addcomment(request, article_id):
    if request.POST and ("pause" not in request.session):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comments_article = Article.objects.get(id=article_id)

            user_id = auth.get_user(request).id
            comment.comments_from = User.objects.get(id=user_id)
            comment.comments_date = datetime.now()


            form.save()
            request.session.set_expiry(60)
            request.session['pause'] = True
    return redirect('/articles/get/%s/' % article_id)


