# Generated by Django 5.0.1 on 2024-01-23 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0013_genres'),
    ]

    operations = [
        migrations.AddField(
            model_name='genres',
            name='genre_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]