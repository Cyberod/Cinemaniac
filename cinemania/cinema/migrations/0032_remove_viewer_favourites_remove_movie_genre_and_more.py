# Generated by Django 5.0.1 on 2024-02-01 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0031_alter_viewer_f_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='viewer',
            name='favourites',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='genre',
        ),
        migrations.RemoveField(
            model_name='viewer',
            name='F_name',
        ),
        migrations.DeleteModel(
            name='FavouriteMovie',
        ),
        migrations.DeleteModel(
            name='Movie',
        ),
        migrations.DeleteModel(
            name='Viewer',
        ),
    ]
