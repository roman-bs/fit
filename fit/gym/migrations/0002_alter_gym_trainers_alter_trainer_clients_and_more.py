# Generated by Django 4.0.1 on 2022-04-03 12:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gym', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gym',
            name='trainers',
            field=models.ManyToManyField(blank=True, to='gym.Trainer'),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='clients',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='trainer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='gyms',
            field=models.ManyToManyField(blank=True, to='gym.Gym'),
        ),
    ]
