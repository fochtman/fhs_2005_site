# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fhsuser',
            old_name='ticket_num',
            new_name='num_ticket',
        ),
        migrations.AddField(
            model_name='fhsuser',
            name='num_kids',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='fhsuser',
            name='profession',
            field=models.CharField(default='Boob', max_length=50),
            preserve_default=False,
        ),
    ]
