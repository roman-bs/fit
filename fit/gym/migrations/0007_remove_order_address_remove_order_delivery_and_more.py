# Generated by Django 4.0.3 on 2022-04-04 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0006_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='address',
        ),
        migrations.RemoveField(
            model_name='order',
            name='delivery',
        ),
        migrations.RemoveField(
            model_name='order',
            name='postal_code',
        ),
    ]
