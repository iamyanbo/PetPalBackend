# Generated by Django 4.2.6 on 2023-12-06 20:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('applications', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('rating', models.PositiveIntegerField(blank=True, null=True)),
                ('is_author_seeker', models.BooleanField()),
                ('is_review', models.BooleanField()),
                ('application', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='applications.application')),
                ('seeker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seeker_comments', to=settings.AUTH_USER_MODEL)),
                ('shelter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shelter_comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
