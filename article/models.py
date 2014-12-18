# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    class Meta():
        db_table = "article"
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
    article_title = models.CharField(max_length = 200)
    article_text = models.TextField(blank=True, null=True)
    article_date = models.DateTimeField()
    article_likes = models.IntegerField(default=0)

    img_width = models.PositiveIntegerField(default="150")

    article_image = models.ImageField(upload_to="static",
                                      width_field="img_width",
                                      verbose_name="Фото",
                                      default="default.png",
                                      blank=True)


    def __unicode__(self):
        return self.article_title


class Comments(models.Model):
    class Meta():
        db_table = 'Comments'
    comments_date = models.DateTimeField()
    comments_text = models.TextField(max_length=300, verbose_name="Текст комментария:")
    comments_article = models.ForeignKey(Article)
    comments_from = models.ForeignKey(User)

