# Generated by Django 2.2.10 on 2020-04-16 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0042_auto_20200416_1808'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='addition_fields',
            new_name='fields_info',
        ),
    ]
