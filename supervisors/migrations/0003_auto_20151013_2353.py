# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supervisors', '0002_auto_20151013_2204'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supervisors',
            old_name='pastor',
            new_name='pastor_user_profile',
        ),
        migrations.RenameField(
            model_name='supervisors',
            old_name='user_profile',
            new_name='supervisor_user_profile',
        ),
    ]
