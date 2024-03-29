# Generated by Django 5.0.1 on 2024-01-30 23:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0021_rename_user_name_favourites_viewer_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='favourites',
            old_name='viewer',
            new_name='user_name',
        ),
        migrations.RemoveField(
            model_name='movies',
            name='viewer',
        ),
        migrations.AddField(
            model_name='movies',
            name='favourite_status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cinema.favourites'),
        ),
    ]
