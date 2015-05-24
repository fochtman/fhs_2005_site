# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20150523_0310'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fhsuser',
            name='id',
        ),
        migrations.AlterField(
            model_name='fhsuser',
            name='user',
            field=models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
