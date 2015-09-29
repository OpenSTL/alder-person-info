# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0007_vote_ward'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='ward',
            field=models.ForeignKey(related_name='votes', default=0, to='votes.Ward'),
        ),
    ]
