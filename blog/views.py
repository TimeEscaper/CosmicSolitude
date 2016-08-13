# _*_ coding: utf-8 _*_

from django.shortcuts import render
from django.http import Http404
from django.views.decorators.csrf import csrf_protect
from models import Article, Tag, Rubric
from django.utils import html

# Create your views here.

def index_display(request):
    return render(request, 'index.html', {
        'page_title': u'Main',
        'menu_index': '1',
    })

def article_display(request):
    return render(request, 'article.html', {
        'page_title': u'Title',
        'menu_index': '2',
    })

def new_article_display(request):
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
        })
    new_title = request.POST.get('title','')
    new_slug = request.POST.get('slug','')
    new_rubric = request.POST.get('rubric','')
    new_is_hidden = request.POST.get('is_hidden', False)
    new_text = request.POST.get('text','')
    has_empty = False
    error_text = u'Поля'
    if new_title == '':
        has_empty = True
        error_text = error_text + u' Заголовок,'
    if new_slug == '':
        has_empty = True
        error_text = error_text + u' Slug,'
    if new_rubric == '':
        has_empty = True
        error_text = error_text + u' Рубрика,'
    if new_text == '':
        has_empty = True
        error_text = error_text + u' Текст,'
    if has_empty is True:
        error_text = error_text[:-1]
        error_text = error_text + u' не заполнены!'
        return render(request, 'new.html', {
            'page_title': u'Новая статья',
            'menu_index': '2',
            'error_code': '1',
            'error_text': error_text,
            'input_title': new_title,
            'input_slug': new_slug,
            'input_rubric': new_rubric,
            'input_is_hidden': is_hidden,
            'input_text': new_text,
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
            'input_is_hidden': is_hidden,
            'input_text': new_text,
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
            'input_is_hidden': is_hidden,
            'input_text': new_text,
        })
    html.strip_tags(new_title)
    html.strip_tags(new_slug)
    html.strip_tags(new_rubric)
    html.strip_tags(new_text)




def article_publish(request):
    if not request.User.is_authenticated():
        return Http404
