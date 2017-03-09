# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='profile_image',
            field=models.FileField(upload_to=b'documents/%Y/%m/%d', blank=True),
            preserve_default=True,
        ),
    ]
