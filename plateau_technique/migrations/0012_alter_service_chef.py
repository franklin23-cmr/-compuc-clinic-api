# Generated by Django 3.2.5 on 2021-09-09 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grh', '0019_personnel_should_update_password'),
        ('plateau_technique', '0011_infrastructurepersonnel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='chef',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='grh.personnel'),
        ),
    ]
