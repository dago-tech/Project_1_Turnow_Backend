# Generated by Django 4.2.7 on 2023-11-14 03:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('desks', '0001_initial'),
        ('categories', '0001_initial'),
        ('priorities', '0001_initial'),
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Turn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('turn_number', models.CharField(blank=True, default='0', max_length=4, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('start_time', models.TimeField(blank=True, null=True)),
                ('end_time', models.TimeField(blank=True, null=True)),
                ('duration', models.IntegerField(blank=True, null=True)),
                ('state', models.CharField(choices=[('pending', 'Pending'), ('serving', 'Serving'), ('served', 'Served'), ('first to serve', 'First to serve'), ('cancelled', 'Cancelled')], default='pending')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.category')),
                ('desk', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='desks.desk')),
                ('personal_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.client')),
                ('priority', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='priorities.priority')),
            ],
        ),
    ]
