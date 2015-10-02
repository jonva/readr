# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_readr', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.CharField(max_length=300, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='body',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='downvotes',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='img_primary',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='img_secondary',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='published_on',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='upvotes',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
    ]
