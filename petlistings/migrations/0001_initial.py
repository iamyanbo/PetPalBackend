# Generated by Django 4.2.6 on 2023-12-06 20:25

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
            name='PetListing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('category', models.CharField(choices=[('D', 'Dog'), ('C', 'Cat'), ('O', 'Other')], max_length=1)),
                ('breed', models.CharField(blank=True, max_length=255)),
                ('age', models.PositiveIntegerField(blank=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('X', 'Unknown')], max_length=1)),
                ('size', models.CharField(choices=[('L', 'Large'), ('M', 'Mid'), ('S', 'Small')], max_length=1)),
                ('status', models.CharField(choices=[('AV', 'Available'), ('AD', 'Adopted'), ('PE', 'Pending'), ('WI', 'Withdrawn')], default='AV', max_length=2)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('med_history', models.TextField(blank=True, null=True)),
                ('behaviour', models.TextField(blank=True, null=True)),
                ('special_needs', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True)),
                ('favorited_by', models.ManyToManyField(related_name='favorited_pets', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='petlistings', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'pet listing',
            },
        ),
        migrations.CreateModel(
            name='PetListingImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='pet-images/')),
                ('petlisting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='petlistings.petlisting')),
            ],
            options={
                'verbose_name': 'pet listing image',
            },
        ),
    ]
