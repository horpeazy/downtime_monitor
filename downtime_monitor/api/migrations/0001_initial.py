# Generated by Django 4.1.5 on 2023-01-08 02:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('auth_scheme', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='DowntimeLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('down_time', models.DateTimeField(blank=True, null=True)),
                ('up_time', models.DateTimeField(blank=True, null=True)),
                ('website', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.website')),
            ],
        ),
    ]
