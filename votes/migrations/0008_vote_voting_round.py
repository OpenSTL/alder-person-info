# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0007_bill_votinground'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='voting_round',
            field=models.ForeignKey(default=0, to='votes.VotingRound'),
        ),
    ]
