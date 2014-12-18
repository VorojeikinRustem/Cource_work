# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0012_auto_20141219_0105'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='article_image',
        ),
        migrations.RemoveField(
            model_name='article',
            name='url_width',
        ),
    ]
