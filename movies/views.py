from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import Movie,Category
from .serializer import MovieSerializer,MovieCatSerializer

class MovieListCreateView(ListCreateAPIView):
    serializer_class=MovieSerializer
    queryset=Movie.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['title',]


class MovieRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class=MovieSerializer
    lookup_field='id'
    queryset=Movie.objects.all()


class MovieCategoryView(ListCreateAPIView):
    serializer_class=MovieCatSerializer
    queryset=Category.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', ]
