# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-06 02:21


from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0019_auto_20180206_0155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_author_set', to='events.Participant'),
        ),
    ]
