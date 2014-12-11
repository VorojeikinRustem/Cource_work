# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_comments_comments_date'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='comments',
            table='Comments',
        ),
    ]
