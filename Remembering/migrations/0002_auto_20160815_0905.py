# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-15 09:05
from __future__ import unicode_literals

import Remembering.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Remembering', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=Remembering.models.get_file_path),
        ),
    ]