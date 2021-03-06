from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'firstapp.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^articles/all/$', 'article.views.articles'),
                       url(r'^about/$', 'article.views.about'),
                       url(r'^articles/get/(?P<article_id>\d+)/$', 'article.views.article'),
                       url(r'^articles/addlike/(?P<article_id>\d+)/$', 'article.views.addlike'),
                       url(r'^articles/addcomment/(?P<article_id>\d+)/$', 'article.views.addcomment'),
                       url(r'^page/(\d+)/$', 'article.views.articles'),
                       url(r'^', 'article.views.index'),

                       )