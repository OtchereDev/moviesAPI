from django.urls import path

from .views import MovieListCreateView,MovieRetrieveUpdateDestroyAPIView,MovieCategoryView


app_name='movies_api'

urlpatterns = [
    path('',MovieListCreateView.as_view()),
    path('cat/',MovieCategoryView.as_view()),
    path('<int:id>/',MovieRetrieveUpdateDestroyAPIView.as_view()),
]
