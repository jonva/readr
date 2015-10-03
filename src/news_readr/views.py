from django.shortcuts import render
from .models import Article

# Create your views here.
def home(request):
    title = "Home"
    article_list = Article.objects.all().order_by('-published_on')
    context = {
               "title": title,
               "article_list": article_list,
               }
    return render(request, "home.html", context)

def details(request, article_id='1'):
    article = Article.objects.get(id=article_id)
    return render(request, "details.html", {'article': article})