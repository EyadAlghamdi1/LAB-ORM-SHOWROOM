# Generated by Django 5.1.2 on 2024-11-21 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='fuel_type',
            field=models.BooleanField(),
        ),
    ]