# Generated by Django 3.1.2 on 2021-11-01 16:04

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
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(max_length=300)),
                ('title', models.CharField(max_length=500)),
                ('item_url', models.CharField(max_length=200)),
                ('desc', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Side_search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(max_length=300)),
                ('item', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Top_search_first',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(max_length=300)),
                ('item', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Top_search_second',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(max_length=300)),
                ('item', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('residential_address', models.CharField(blank=True, max_length=500)),
                ('state_of_origin', models.CharField(blank=True, max_length=100)),
                ('favorite_food', models.CharField(blank=True, max_length=200)),
                ('about', models.TextField(blank=True, max_length=700)),
                ('photo', models.FileField(blank=True, null=True, upload_to='images/', verbose_name='')),
                ('user', models.OneToOneField(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
