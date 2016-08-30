# _*_ coding: utf-8 _*_

from django.contrib import admin
from models import Article, Rubric, Tag, ArticleView



class RubricAdmin(admin.ModelAdmin):
	pass

class TagAdmin(admin.ModelAdmin):
	pass

class ArticleAdmin(admin.ModelAdmin):
	pass

class ArticleViewAdmin(admin.ModelAdmin):
	pass

admin.site.register(Rubric, RubricAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleView, ArticleViewAdmin)