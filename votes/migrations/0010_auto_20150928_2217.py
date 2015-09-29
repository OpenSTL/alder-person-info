# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0009_remove_vote_ward'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Ward',
        ),
        migrations.AddField(
            model_name='vote',
            name='ward_number',
            field=models.CharField(default=b'0', max_length=100),
        ),
    ]
