# Generated by Django 3.2.6 on 2021-08-28 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20210828_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='partial',
            name='harvester_id',
            field=models.CharField(default=None, max_length=64, null=True),
        ),
    ]
