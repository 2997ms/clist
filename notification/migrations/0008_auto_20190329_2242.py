# Generated by Django 2.1.7 on 2019-03-29 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0007_auto_20180520_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='period',
            field=models.CharField(choices=[('', '...'), ('event', 'Event'), ('hour', 'Hour'), ('day', 'Day'), ('week', 'Week'), ('month', 'Month')], max_length=16),
        ),
    ]
