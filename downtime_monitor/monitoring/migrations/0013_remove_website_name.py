# Generated by Django 4.1.5 on 2023-01-11 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0012_rename_alias_monitor_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='website',
            name='name',
        ),
    ]
