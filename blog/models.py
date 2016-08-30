# _*_ coding: utf-8 _*_

from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length = 20, verbose_name = u"Название")

    class Meta:
        verbose_name = u"Тег"
        verbose_name_plural = u"Теги"

    def __unicode__(self):
        return self.name

class Rubric(models.Model):
    name = models.CharField(max_length = 40, verbose_name = u"Название")

    class Meta:
        verbose_name = u"Рубрика"
        verbose_name_plural = u"Рубрики"

    def __unicode__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length = 255, verbose_name = u"Заголовок")
    date = models.DateTimeField(verbose_name = u"Дата")
    is_hidden = models.BooleanField(verbose_name = u"Скрытая статья")
    is_deleted = models.BooleanField(verbose_name = u"Удалено")
    is_published = models.BooleanField(verbose_name = u"Опубликовано")
    text = models.TextField(verbose_name = u"Текст")
    slug = models.CharField(max_length = 255, verbose_name = u"Slug")
    image = models.ImageField(blank = True)
    tags = models.ManyToManyField(Tag, verbose_name = u"Теги")
    rubric = models.ForeignKey(Rubric, verbose_name = u"Рубрика")

    class Meta:
        verbose_name = u"Статья"
        verbose_name_plural = u"Статьи"

class ArticleView(models.Model):
    ip_address = models.GenericIPAddressField(verbose_name = u"IP")
    view_article = models.ForeignKey(Article, verbose_name = u"Статья")

    class Meta:
        verbose_name = u"Просмотр"
        verbose_name_plural = u"Просмотры"
