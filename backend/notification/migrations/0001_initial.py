# Generated by Django 4.2.6 on 2023-10-12 21:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200)),
                ('body', models.CharField(max_length=200)),
                ('view', models.CharField(choices=[('s', 'seen'), ('u', 'unseen')], default='u', max_length=100)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notif_receiver', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notif_sender', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
