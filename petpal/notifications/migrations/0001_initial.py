# Generated by Django 4.2.6 on 2023-11-13 20:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.TextField()),
                ('body', models.TextField(blank=True)),
                ('object_id', models.PositiveIntegerField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('recipients', models.ManyToManyField(related_name='notifications', to=settings.AUTH_USER_MODEL)),
                ('recipients_read', models.ManyToManyField(blank=True, related_name='notifications_read', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]