# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-03 00:46


from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='deadline_registration',
            new_name='registration_deadline',
        ),
    ]
