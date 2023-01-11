# Generated by Django 4.1.5 on 2023-01-09 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0002_downtimelog_error'),
    ]

    operations = [
        migrations.AddField(
            model_name='website',
            name='name',
            field=models.CharField(default='Testwebsite', max_length=60),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='website',
            name='auth_scheme',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='website',
            name='url',
            field=models.URLField(unique=True),
        ),
    ]