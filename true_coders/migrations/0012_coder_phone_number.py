# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-05 22:27


from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('true_coders', '0011_coder_middle_name_native'),
    ]

    operations = [
        migrations.AddField(
            model_name='coder',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128),
        ),
    ]
