# Generated by Django 3.0.3 on 2020-03-02 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0008_auto_20200228_0813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='réalisateur'),
        ),
    ]
