# Generated by Django 3.0.3 on 2020-02-27 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_auto_20200227_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movierent',
            name='date_retur',
            field=models.DateField(blank=True, null=True),
        ),
    ]