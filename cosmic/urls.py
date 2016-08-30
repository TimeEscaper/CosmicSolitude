"""cosmic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from blog import views as blog_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', blog_view.index_display, name = "index_display"),
    url(r'^blog/sample-article/$', blog_view.sample_article_display, name = "sample-article_display"),
    url(r'^blog/new/$', blog_view.new_article_display, name = "new_article_display"),
    url(r'^blog/article/(?P<slug>[A-Za-z0-9\-]+)/$', blog_view.article_display, name = "article_display"),
]
