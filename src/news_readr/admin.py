from django.contrib import admin

from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'added_on']
#     class Meta:
#         model = Article
        
admin.site.register(Article, ArticleAdmin)
