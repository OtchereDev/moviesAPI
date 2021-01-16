from rest_framework import serializers


from .models import Movie,Category


class MovieCatSerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['name',]

class MovieSerializer(serializers.ModelSerializer):
    category=MovieCatSerializer()
    class Meta:
        model=Movie
        fields=['title',
            'category',
            'description',
            'directors',
            'release_date',
            'movie_file',]