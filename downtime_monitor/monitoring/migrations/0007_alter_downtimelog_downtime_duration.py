# Generated by Django 4.1.5 on 2023-01-09 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0006_alter_downtimelog_downtime_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='downtimelog',
            name='downtime_duration',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]