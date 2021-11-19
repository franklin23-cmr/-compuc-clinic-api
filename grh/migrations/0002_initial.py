# Generated by Django 3.2.5 on 2021-08-01 10:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('grh', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('plateau_technique', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='poste',
            name='service',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='plateau_technique.service'),
        ),
        migrations.AddField(
            model_name='poste',
            name='unite',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='plateau_technique.unitemedicale'),
        ),
        migrations.AddField(
            model_name='pointage',
            name='personnel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grh.personnel'),
        ),
        migrations.AddField(
            model_name='personnel',
            name='personnel',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='personnel',
            name='poste',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='grh.poste'),
        ),
        migrations.AddField(
            model_name='permission',
            name='personnel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grh.personnel'),
        ),
        migrations.AddField(
            model_name='absence',
            name='personnel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grh.personnel'),
        ),
        migrations.AddField(
            model_name='stage',
            name='stagiaire',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='grh.stagiaire'),
        ),
        migrations.AddField(
            model_name='profilspecialiste',
            name='medecin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grh.medecin'),
        ),
    ]
