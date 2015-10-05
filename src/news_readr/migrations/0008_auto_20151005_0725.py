# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_readr', '0007_auto_20151004_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.CharField(default=b'Anonymous Author', max_length=300, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='img_secondary',
            field=models.ImageField(default=b'../static/news_readr/img/404.jpg', null=True, upload_to=b'img_secondary', blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(default=b'No title available', max_length=300, null=True),
        ),
    ]
