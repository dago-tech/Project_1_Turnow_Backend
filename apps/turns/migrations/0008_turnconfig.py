# Generated by Django 4.2.7 on 2024-01-01 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turns', '0007_alter_turn_desk'),
    ]

    operations = [
        migrations.CreateModel(
            name='TurnConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restart_turn', models.BooleanField(default=False)),
            ],
        ),
    ]
