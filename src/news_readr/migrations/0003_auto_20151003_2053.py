# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_readr', '0002_auto_20150928_1946'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='summary',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='img_primary',
            field=models.ImageField(null=True, upload_to=b'img', blank=True),
        ),
    ]
