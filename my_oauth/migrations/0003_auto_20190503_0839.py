# Generated by Django 2.1.7 on 2019-05-03 08:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_oauth', '0002_auto_20190329_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='coder',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='true_coders.Coder'),
        ),
    ]
