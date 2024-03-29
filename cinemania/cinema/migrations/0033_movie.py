# Generated by Django 5.0.1 on 2024-02-01 19:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0032_remove_viewer_favourites_remove_movie_genre_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('description', models.TextField(null=True)),
                ('release_date', models.DateField(null=True)),
                ('genre', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cinema.genre')),
            ],
        ),
    ]
