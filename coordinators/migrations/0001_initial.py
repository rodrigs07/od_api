# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('supervisors', '0003_auto_20151013_2353'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coordinators',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cordinator_user_profile', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('supervisor_user_profile', models.ForeignKey(to='supervisors.Supervisors')),
            ],
        ),
    ]
