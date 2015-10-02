from django.shortcuts import render
from .models import Article

# Create your views here.
def home(request):
    title = "Home"
    article_list = Article.objects.all()
    for article in article_list:
        print(article.id)
    context = {
               "title": title,
               "article_list": article_list,
               }
    return render(request, "home.html", context)

def details(request):
    article = Article.objects.get(id='1')
    return render(request, "details.html", {'article': article})