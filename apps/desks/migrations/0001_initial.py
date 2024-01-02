# Generated by Django 4.2.7 on 2023-11-14 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Desk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('state', models.BooleanField(default=True)),
                ('busy', models.BooleanField(default=False)),
                ('category', models.ManyToManyField(to='categories.category')),
            ],
        ),
    ]
