# Generated by Django 2.1.7 on 2019-08-18 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('true_coders', '0020_remove_filter_categories'),
    ]

    operations = [
        migrations.RenameField(
            model_name='filter',
            old_name='arr_categories',
            new_name='categories',
        ),
    ]
