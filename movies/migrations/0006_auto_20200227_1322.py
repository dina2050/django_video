# Generated by Django 3.0.3 on 2020-02-27 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_movierent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movierent',
            name='date_out',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='movierent',
            name='date_retur',
            field=models.DateField(null=True),
        ),
    ]
