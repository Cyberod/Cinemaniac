# Generated by Django 5.0.1 on 2024-01-23 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0011_remove_movies_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favourites',
            name='genre',
        ),
        migrations.RemoveField(
            model_name='favourites',
            name='movie_name',
        ),
        migrations.RemoveField(
            model_name='favourites',
            name='user_name',
        ),
        migrations.AddField(
            model_name='movies',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Genres',
        ),
        migrations.DeleteModel(
            name='Favourites',
        ),
    ]
