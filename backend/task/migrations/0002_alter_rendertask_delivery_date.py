# Generated by Django 4.2.5 on 2023-09-27 13:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rendertask',
            name='delivery_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
