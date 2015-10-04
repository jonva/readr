from .models import Article
def media_url(request):
    from django.conf import settings
    return {'media_url': settings.MEDIA_URL}


def toreads(request):
    toreads = Article.objects.order_by('?')[:4]
    for toread in toreads:
        toread.title = toread.title[:100] + (toread.title[100:] and '..')
        toread.summary = toread.summary[:100] + (toread.summary[100:] and '..')
    return {'toreads': toreads}