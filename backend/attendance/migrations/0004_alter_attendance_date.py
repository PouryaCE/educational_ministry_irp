# Generated by Django 4.2.6 on 2023-10-13 08:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0003_alter_attendance_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='تاریخ'),
        ),
    ]
