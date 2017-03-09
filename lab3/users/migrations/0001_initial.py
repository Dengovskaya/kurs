# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'first name', max_length=30)),
                ('surname', models.CharField(default=b'second name', max_length=30)),
                ('phone', models.CharField(max_length=20, blank=True)),
                ('about', models.CharField(max_length=255, blank=True)),
                ('profile_image', models.ImageField(upload_to=b'documents/%Y/%m/%d', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
