# Generated by Django 4.2.7 on 2023-11-25 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='personal_id',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
