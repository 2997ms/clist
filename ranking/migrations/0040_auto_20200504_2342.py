# Generated by Django 2.2.10 on 2020-05-04 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ranking', '0039_auto_20200503_2222'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='account',
            index=models.Index(fields=['resource', 'n_contests'], name='ranking_acc_resourc_23c237_idx'),
        ),
    ]
