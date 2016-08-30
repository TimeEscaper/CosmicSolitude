# _*_ coding: utf-8 _*_

from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import Http404, HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from models import Article, Tag, Rubric
from django.utils import html
import datetime
import logging
# Create your views here.

def index_display(request):
    return render(request, 'index.html', {
        'page_title': u'Main',
        'menu_index': '1',
    })

def sample_article_display(request):
    return render(request, 'sample_article.html', {
        'page_title': u'Title',
        'menu_index': '2',
    })

def new_article_display(request):
    if not request.user.is_authenticated():
        return Http404
    if request.method != 'POST':
        return render(request, 'new.html', {
            'page_title': u'Новая статья',
            'menu_index': '2',
            'error_code': '0',
            'input_title': '',
            'input_slug': '',
            'input_rubric': '',
            'input_is_hidden': '',
            'input_text': '',
            'input_tags': '',
            'rubrics': Rubric.objects.all(),
        })
    new_title = request.POST.get('title','').encode('utf-8')
    new_slug = request.POST.get('slug','').encode('utf-8')
    new_rubric = request.POST.get('rubric', 1)
    logging.error(new_rubric)
    new_is_hidden = request.POST.get('is_hidden', False)
    new_text = request.POST.get('text','').encode('utf-8')
    new_tags = request.POST.get('tags', '').encode('utf-8')
    error_count = 0
    error_text = u''
    if new_title == '':
        error_text = error_text + u' Заголовок,'
        error_count = error_count + 1
    if new_slug == '':
        error_text = error_text + u' Slug,'
        error_count = error_count + 1
    if new_rubric == '':
        error_text = error_text + u' Рубрика,'
        error_count = error_count + 1
    if new_text == '':
        error_text = error_text + u' Текст,'
        error_count = error_count + 1
    if error_count is not 0:
        error_text = error_text[:-1]
        if error_count == 1:
            error_text = u'Поле' + error_text + u' не заполнено!'
        else:
            error_text = u'Поля' + error_text + u' не заполнены!'
        return render(request, 'new.html', {
            'page_title': u'Новая статья',
            'menu_index': '2',
            'error_code': '1',
            'error_text': error_text,
            'input_title': new_title,
            'input_slug': new_slug,
            'input_rubric': new_rubric,
            'input_is_hidden': new_is_hidden,
            'input_text': new_text,
            'input_tags': new_tags,
            'rubrics': Rubric.objects.all(),
        })
    if Article.objects.filter(title = new_title).exists():
        return render(request, 'new.html', {
            'page_title': u'Новая статья',
            'menu_index': '2',
            'error_code': '2',
            'error_text': u'Статья с таким заголовком уже есть!',
            'input_title': new_title,
            'input_slug': new_slug,
            'input_rubric': new_rubric,
            'input_is_hidden': new_is_hidden,
            'input_text': new_text,
            'input_tags': new_tags,
            'rubrics': Rubric.objects.all(),
        })
    if Article.objects.filter(slug = new_slug).exists():
        return render(request, 'new.html', {
            'page_title': u'Новая статья',
            'menu_index': '2',
            'error_code': '3',
            'error_text': u'Статья с таким slug уже есть!',
            'input_title': new_title,
            'input_slug': new_slug,
            'input_rubric': new_rubric,
            'input_is_hidden': new_is_hidden,
            'input_text': new_text,
            'input_tags': new_tags,
            'rubrics': Rubric.objects.all(),
        })
    if not Rubric.objects.filter(id = new_rubric).exists():
        return render(request, 'new.html', {
            'page_title': u'Новая статья',
            'menu_index': '2',
            'error_code': '4',
            'error_text': u'Нет такой рубрики!',
            'input_title': new_title,
            'input_slug': new_slug,
            'input_rubric': new_rubric,
            'input_is_hidden': new_is_hidden,
            'input_text': new_text,
            'input_tags': new_tags,
            'rubrics': Rubric.objects.all(),
        })
    html.strip_tags(new_title)
    html.strip_tags(new_slug)
    html.strip_tags(new_rubric)
    html.strip_tags(new_text)
    html.strip_tags(new_tags)
    new_article = Article(title = new_title,
        date = datetime.datetime.now(),
        slug = new_slug,
        rubric = Rubric.objects.filter(id = new_rubric),
        text = new_text,
        is_hidden = new_is_hidden,
        is_deleted = False,
        is_published = True)
    new_article.save()
    for tag_str in new_tags.split(','):
        if Tag.objects.filter(name = tag_str).exists():
            tag = Tag.objects.get(name = tag_str)
            new_article.tags.add(tag)
        else:
            tag = Tag(name = tag_str)
            tag.save()
            new_article.tags.add(tag)
    return HttpResponseRedirect('/blog/article/{}'.format(new_slug))

def article_display(request, slug):
    article = Article.objects.get(slug = slug)
    if article is None:
        return Http404
    if article.is_deleted is True or article.is_published is False:
        return Http404
    if article.is_hidden is True and not request.user.is_authenticated():
        return Http404
    return render(request, 'article.html', {
            'page_title': article.title,
            'menu_index': '2',
            'article': article,
        })