# Generated by Django 3.1 on 2020-08-22 14:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0004_auto_20200821_0929'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='day and time'),
            preserve_default=False,
        ),
    ]
