# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pastors', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pastors',
            old_name='pastor',
            new_name='city',
        ),
        migrations.AddField(
            model_name='pastors',
            name='state',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
