# Generated by Django 3.2.5 on 2021-08-31 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grh', '0007_alter_periode_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='periode',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='periode',
            name='day',
            field=models.PositiveSmallIntegerField(choices=[(0, 'lundi'), (1, 'mardi'), (2, 'mercredi'), (3, 'jeudi'), (4, 'vendredi'), (5, 'samedi'), (6, 'dimanche')], default=0, null=True),
        ),
    ]
