# Generated by Django 3.2.5 on 2021-09-13 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultation', '0013_auto_20210910_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescriptionexamen',
            name='label',
            field=models.CharField(default='', max_length=50),
        ),
    ]
