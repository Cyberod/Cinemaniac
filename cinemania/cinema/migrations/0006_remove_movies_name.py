# Generated by Django 5.0.1 on 2024-01-23 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0005_remove_genres_genre_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movies',
            name='name',
        ),
    ]
