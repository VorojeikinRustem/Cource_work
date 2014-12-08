# -*- coding: utf-8 -*-
from django.db import models

class Article(models.Model):
    class Meta():
        db_table ="article"
    article_title = models.CharField(max_length = 200)
    article_text = models.TextField()
    article_date = models.DateTimeField()
    article_likes = models.IntegerField(default=True)

class Comments(models.Model):
    class Meta():
        db_table = 'Comments'
    comments_text = models.TextField(verbose_name="Комментарии:")
    comments_article = models.ForeignKey(Article)