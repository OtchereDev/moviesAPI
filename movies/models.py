from django.db import models

from .validators import validate_file_extension


class Movie(models.Model):
    title=models.CharField(max_length=500)
    category=models.ForeignKey('category',on_delete=models.CASCADE)
    description = models.TextField()
    directors=models.CharField(max_length=225)
    release_date=models.DateField()
    movie_file=models.FileField(validators=[validate_file_extension,])


class Category(models.Model):
    name=models.CharField(max_length=225)