# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-05 04:39


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0011_auto_20180204_2344'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='website_url',
            field=models.URLField(default=None, null=True),
            preserve_default=False,
        ),
    ]
