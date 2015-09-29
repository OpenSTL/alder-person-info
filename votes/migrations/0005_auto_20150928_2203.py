# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0004_vote_ward_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ward_number', models.CharField(default=b'0', max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='vote',
            name='ward_number',
        ),
        migrations.AddField(
            model_name='vote',
            name='ward',
            field=models.ForeignKey(related_name='votes', default=datetime.datetime(2015, 9, 28, 22, 3, 50, 903797, tzinfo=utc), to='votes.Ward'),
            preserve_default=False,
        ),
    ]
