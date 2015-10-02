from django.db import models

class Article(models.Model):
    title = models.CharField(
        max_length=300,
        blank=False, 
        null=True
        )
    author = models.CharField(
        max_length=300,
        blank=True, 
        null=True
        )
    published_on = models.DateTimeField(blank=True, null=True)
    category = models.CharField(max_length=200, blank=True, null=True)
    img_primary = models.ImageField(blank=True, null=True)
    img_secondary = models.ImageField(blank=True, null=True)
    body = models.TextField(
        blank=True,
        null=True
        )
    upvotes = models.IntegerField(
        default = 0,
        blank=True, 
        null=True
        )
    downvotes = models.IntegerField(
        default = 0,
        blank=True, 
        null=True
        )
    added_on = models.DateTimeField(auto_now_add=True, auto_now=False, blank=False, null=False)
    updated_on = models.DateTimeField(auto_now_add=False, auto_now=True, blank=False, null=False)