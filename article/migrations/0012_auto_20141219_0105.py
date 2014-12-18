# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0011_auto_20141219_0104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_image',
            field=models.ImageField(default=b'article/static/default.png', width_field=b'url_width', upload_to=b'article/static/', blank=True, verbose_name=b'\xd0\xa4\xd0\xbe\xd1\x82\xd0\xbe'),
            preserve_default=True,
        ),
    ]
