# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-09-24 01:01


from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('true_coders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('chat_id', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('secret_key', models.CharField(blank=True, max_length=20, null=True)),
                ('last_command', jsonfield.fields.JSONField(blank=True, default={})),
                ('coder', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='true_coders.Coder')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('message', jsonfield.fields.JSONField(default=dict)),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tg.Chat')),
            ],
            options={
                'ordering': ['-created'],
                'verbose_name_plural': 'History',
            },
        ),
    ]
