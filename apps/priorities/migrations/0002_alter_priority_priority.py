# Generated by Django 4.2.7 on 2023-11-15 20:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('priorities', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='priority',
            name='priority',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(limit_value=20)]),
        ),
    ]