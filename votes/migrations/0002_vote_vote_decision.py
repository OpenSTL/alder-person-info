# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='vote_decision',
            field=models.CharField(default=b'Present', max_length=100),
        ),
    ]
