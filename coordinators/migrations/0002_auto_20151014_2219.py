# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coordinators', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coordinators',
            old_name='cordinator_user_profile',
            new_name='coordinator_user_profile',
        ),
    ]
