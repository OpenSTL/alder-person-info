# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0005_ward'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vote',
            name='ward_number',
        ),
        migrations.AddField(
            model_name='vote',
            name='ward',
            field=models.ForeignKey(default=0, to='votes.Ward'),
        ),
    ]
