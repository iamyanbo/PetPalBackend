# Generated by Django 4.2.6 on 2023-11-13 20:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('petlistings', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=255)),
                ('contact_pref', models.CharField(choices=[('P', 'Phone Call'), ('T', 'Text'), ('E', 'Email')], max_length=1)),
                ('pet_number', models.IntegerField()),
                ('has_children', models.BooleanField()),
                ('experience', models.CharField(choices=[('EX', 'Experienced'), ('IN', 'Intermediate'), ('NE', 'No Experience')], max_length=2)),
                ('residence_type', models.CharField(choices=[('C', 'Condo'), ('A', 'Apartment'), ('H', 'House')], max_length=1)),
                ('status', models.CharField(choices=[('P', 'Pending'), ('A', 'Approved'), ('D', 'Declined'), ('W', 'Withdrawn')], max_length=1)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('petlisting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='petlistings.petlisting')),
                ('seeker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seeker_applications', to=settings.AUTH_USER_MODEL)),
                ('shelter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shelter_applications', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
