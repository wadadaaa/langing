# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import colorful.fields


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='bg_color',
            field=colorful.fields.RGBColorField(blank=True),
            preserve_default=True,
        ),
    ]
