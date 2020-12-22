from django.urls import path

from .views import MovieListCreateView


app_name='movies_api'

urlpatterns = [
    path('',MovieListCreateView.as_view()),
]
