# Generated by Django 5.0.6 on 2024-06-05 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieDatabase', '0004_movie_movie_image_url_movie_movie_short_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='votes',
            field=models.IntegerField(default=0, verbose_name='votes'),
        ),
        migrations.DeleteModel(
            name='Vote',
        ),
    ]