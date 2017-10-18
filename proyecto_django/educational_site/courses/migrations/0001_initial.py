# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-10 22:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=180)),
                ('description', models.TextField()),
            ],
        ),
    ]
