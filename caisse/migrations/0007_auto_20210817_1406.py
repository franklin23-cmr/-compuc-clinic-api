# Generated by Django 3.2.5 on 2021-08-17 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caisse', '0006_alter_bon_date_limite_validite'),
    ]

    operations = [
        migrations.AddField(
            model_name='bon',
            name='_tiaps_generated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='quittance',
            name='_counted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='quittance',
            name='_tiaps_generated',
            field=models.BooleanField(default=False),
        ),
    ]
