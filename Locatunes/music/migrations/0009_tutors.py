# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-21 07:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0008_album_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tutors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poster', models.FileField(upload_to=b'')),
                ('username', models.CharField(max_length=500)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
    ]
