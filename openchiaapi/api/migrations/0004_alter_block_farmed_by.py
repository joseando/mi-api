# Generated by Django 3.2.3 on 2021-07-22 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_delete_points'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='farmed_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.launcher'),
        ),
    ]
