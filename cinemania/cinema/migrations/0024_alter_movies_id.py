# Generated by Django 5.0.1 on 2024-01-31 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0023_alter_movies_options_alter_movies_favourite_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
