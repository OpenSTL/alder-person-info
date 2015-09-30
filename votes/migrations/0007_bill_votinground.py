# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0006_auto_20150929_0220'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bill_number', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='VotingRound',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bill', models.ForeignKey(to='votes.Bill')),
            ],
        ),
    ]
