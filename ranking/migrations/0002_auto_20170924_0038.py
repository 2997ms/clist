# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-09-24 00:38


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('true_coders', '__first__'),
        ('clist', '0006_auto_20170918_0057'),
        ('ranking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='multi_account_allowed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterUniqueTogether(
            name='account',
            unique_together=set([('coder', 'resource', 'key')]),
        ),
    ]
