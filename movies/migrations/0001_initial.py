# Generated by Django 3.0.3 on 2020-02-25 09:06

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MovieGenre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(blank=True, max_length=50, null=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, null=True, populate_from='label')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actors', models.CharField(blank=True, max_length=50, null=True)),
                ('country', models.CharField(blank=True, max_length=50, null=True)),
                ('director', models.CharField(blank=True, max_length=50, null=True)),
                ('length', models.TimeField()),
                ('picture', models.ImageField(upload_to=None)),
                ('release_date', models.DateField()),
                ('rented', models.BooleanField()),
                ('slug', autoslug.fields.AutoSlugField(editable=False, null=True, populate_from='title')),
                ('synopsis', models.TextField(blank=True, null=True)),
                ('title', models.CharField(max_length=50)),
                ('trailer_url', models.URLField()),
                ('genres', models.ManyToManyField(to='movies.MovieGenre')),
            ],
        ),
    ]
