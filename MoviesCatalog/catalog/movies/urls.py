from django.urls import path
from .import views


urlpatterns = [
    path('',views.index, name='movies'), #http://127.0.0.1:8000/movies
    path('<int:movie_id>',views.detail, name='detail'), #http://127.0.0.1:8000/movies\2
    path('search',views.search,name='search'), #http://127.0.0.1:8000/movies/search
]
