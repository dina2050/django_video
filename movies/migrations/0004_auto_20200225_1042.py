# Generated by Django 3.0.3 on 2020-02-25 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20200225_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='trailer_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
