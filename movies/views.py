from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView


from .models import Movie,Category
from .serializer import MovieSerializer,MovieCatSerializer

class MovieListCreateView(ListCreateAPIView):
    serializer_class=MovieSerializer
    queryset=Movie.objects.all()


class MovieRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class=MovieSerializer
    lookup_field='id'
    queryset=Movie.objects.all()


class MovieCategoryView(ListCreateAPIView):
    serializer_class=MovieCatSerializer
    queryset=Category.objects.all()
