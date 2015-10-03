# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_readr', '0003_auto_20151003_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='body',
            field=models.TextField(default=b'No content available', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='summary',
            field=models.TextField(default=b'No caption available', null=True, blank=True),
        ),
    ]
