# Generated by Django 4.2.7 on 2023-12-03 21:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_alter_client_personal_id'),
        ('priorities', '0002_alter_priority_priority'),
        ('categories', '0001_initial'),
        ('turns', '0005_alter_turn_category_alter_turn_personal_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turn',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.category'),
        ),
        migrations.AlterField(
            model_name='turn',
            name='personal_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.client'),
        ),
        migrations.AlterField(
            model_name='turn',
            name='priority',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='priorities.priority'),
        ),
    ]
