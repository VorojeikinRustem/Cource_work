# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_auto_20141212_0053'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='comments_form',
            new_name='comments_from',
        ),
        migrations.AlterField(
            model_name='comments',
            name='comments_date',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
    ]
