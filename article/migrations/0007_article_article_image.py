# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_auto_20141212_0117'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_image',
            field=models.ImageField(default=b'default.png', upload_to=b'static', verbose_name=b'\xd0\xa4\xd0\xbe\xd1\x82\xd0\xbe', blank=True),
            preserve_default=True,
        ),
    ]
