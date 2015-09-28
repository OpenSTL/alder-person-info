# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0002_vote_vote_decision'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='vote_decision',
            field=models.CharField(default=b'Did not vote', max_length=100),
        ),
    ]
