from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView


from .models import Movie
from .serializer import MovieSerializer,MovieCatSerializer

class MovieListCreateView(ListCreateAPIView):
    serializer_class=MovieSerializer
    queryset=Movie.objects.all()



