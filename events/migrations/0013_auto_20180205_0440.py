# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-05 04:40


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0012_event_website_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='website_url',
            field=models.URLField(null=True),
        ),
    ]
