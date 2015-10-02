# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=300)),
                ('author', models.CharField(max_length=300)),
                ('published_on', models.DateTimeField()),
                ('category', models.CharField(max_length=200)),
                ('img_primary', models.ImageField(upload_to=b'')),
                ('img_secondary', models.ImageField(upload_to=b'')),
                ('body', models.TextField(blank=True)),
                ('upvotes', models.IntegerField(default=0)),
                ('downvotes', models.IntegerField(default=0)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
