from django.contrib import admin
from article.models import Article, Comments
from django_markdown.admin import MarkdownModelAdmin

# Register your models here.
class ArticleInline(admin.StackedInline):
    model = Comments
    extra = 2


class ArticleAdmin(MarkdownModelAdmin):
    fields = ['article_title', 'article_text', 'article_date', 'article_image']
    inlines = [ArticleInline]
    list_filter = ['article_date']


admin.site.register(Article, ArticleAdmin)