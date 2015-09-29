# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0008_auto_20150928_2216'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vote',
            name='ward',
        ),
    ]
