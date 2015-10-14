# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('coordinators', '0002_auto_20151014_2219'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Shepherds',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('coordinators_user_profile', models.ForeignKey(to='coordinators.Coordinators')),
                ('shepherds_user_profile', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
