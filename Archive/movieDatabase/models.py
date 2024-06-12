from django.db import models


class Movie(models.Model):
    movie_name = models.CharField(max_length=200)
    movie_short_description = models.CharField(max_length=1000, default="No description available")
    movie_image_url = models.CharField(max_length=1000, default="https://www.kindpng.com/picc/m/18-189751_movie-placeholder-hd-png-download.png")
    movie_pub_date = models.IntegerField("year published")
    votes = models.IntegerField("votes", default=0)
