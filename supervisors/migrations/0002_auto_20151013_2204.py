# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pastors', '0001_initial'),
        ('supervisors', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supervisors',
            name='supervisors',
        ),
        migrations.AddField(
            model_name='supervisors',
            name='pastor',
            field=models.ForeignKey(default=1, to='pastors.Pastors'),
            preserve_default=False,
        ),
    ]
