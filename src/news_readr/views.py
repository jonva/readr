from django.shortcuts import render
from .models import Article
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def home(request):
    title = "Home"
    article_list = Article.objects.all().order_by('-published_on')[:3]
    hero_article = Article.objects.order_by('?')[:1]
    
    for article in article_list:
        article.summary = article.summary[:200] + (article.summary[200:] and '..')
#     if len(article_list) < 1:
#         article_list[0].id = 99999
#         article_list[0].title = "No items in database"
#         article_list[0].summary = "No items in database"
#         article_list[0].body = "No items in database"
#         article_list[0].img_primary = "404.jpg"
#     if len(hero_article) < 1:
#         hero_article[0] = article_list[0]
         
    
    context = {
               "title": title,
               "article_list": article_list,
               "hero_article": hero_article[0]
               }
    return render(request, "home.html", context)

def details(request, article_id = 1):
    try:
        article = Article.objects.get(id=article_id)
        return render(request, "details.html", {'article': article})
    except Article.DoesNotExist:
        article = Article.objects.order_by('?')[:1]
        print(article[0].title)
        return render(request, "details.html", {'article': article[0]})
