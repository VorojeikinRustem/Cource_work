# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20141212_0041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comments_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 11, 21, 43, 54, 966870, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
