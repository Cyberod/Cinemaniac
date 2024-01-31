# Generated by Django 5.0.1 on 2024-01-30 21:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0018_remove_favourites_movie_description_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favourites',
            name='status',
        ),
        migrations.AddField(
            model_name='favourites',
            name='status',
            field=models.ManyToManyField(related_name='status', to=settings.AUTH_USER_MODEL),
        ),
    ]
