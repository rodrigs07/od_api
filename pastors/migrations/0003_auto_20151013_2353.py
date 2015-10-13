# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pastors', '0002_auto_20151013_2222'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pastors',
            old_name='user_profile',
            new_name='pastor_user_profile',
        ),
    ]
