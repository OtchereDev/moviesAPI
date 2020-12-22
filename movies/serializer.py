from rest_framework import serializers


from .models import Movie,Category

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields='__all__'


class MovieCatSerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'