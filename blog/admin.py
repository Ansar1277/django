from django.contrib import admin
from .models import Article, Comment, Tag

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    search_fields = ('title', 'text')

admin.site.register(Comment)
admin.site.register(Tag)

