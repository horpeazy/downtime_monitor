# Generated by Django 4.1.5 on 2023-01-10 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0009_alter_downtimelog_website'),
    ]

    operations = [
        migrations.AlterField(
            model_name='downtimelog',
            name='http_status',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='downtimelog',
            name='response_time',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
