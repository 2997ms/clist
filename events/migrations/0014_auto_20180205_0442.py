# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-05 04:42


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0013_auto_20180205_0440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='website_url',
            field=models.URLField(default=None),
            preserve_default=False,
        ),
    ]
