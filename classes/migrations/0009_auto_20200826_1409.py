# Generated by Django 3.1 on 2020-08-26 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0008_auto_20200825_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='time',
            field=models.CharField(blank=True, choices=[('06:00', '6 a.m.'), ('08:00', '8 a.m.'), ('12:00', '12 p.m.'), ('18:00', '6 p.m.'), ('20:00', '8 p.m')], max_length=10, null=True),
        ),
    ]