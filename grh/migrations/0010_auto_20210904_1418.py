# Generated by Django 3.2.5 on 2021-09-04 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grh', '0009_auto_20210902_1119'),
    ]

    operations = [
        migrations.RenameField(
            model_name='periode',
            old_name='note',
            new_name='description',
        ),
        migrations.AddField(
            model_name='periode',
            name='sujet',
            field=models.CharField(default='Consultation', max_length=100),
        ),
    ]