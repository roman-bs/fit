# Generated by Django 4.0.1 on 2022-03-29 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gyms', '0008_diet_title_gym_title_сoach_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='сlient',
            name='age',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
