# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-06 01:42


from django.db import migrations, models
import django.db.models.deletion
import django_enumfield.db.fields
import events.models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0016_auto_20180206_0132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='event',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='team',
        ),
        migrations.RemoveField(
            model_name='joinrequest',
            name='coder',
        ),
        migrations.RemoveField(
            model_name='joinrequest',
            name='registration',
        ),
        migrations.AddField(
            model_name='joinrequest',
            name='participant',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='events.Participant'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='joinrequest',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='events.Team'),
        ),
        migrations.AddField(
            model_name='team',
            name='event',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='events.Event'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='status',
            field=django_enumfield.db.fields.EnumField(default=9, enum=events.models.TeamStatus),
        ),
        migrations.DeleteModel(
            name='Registration',
        ),
    ]