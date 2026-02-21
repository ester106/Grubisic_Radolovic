from django.urls import path
from .views import *

app_name = "main"

urlpatterns = [
    # Registracija
    path("register/", RegisterView.as_view(), name="register"),

    #Home
    path("", HomeView.as_view(), name="home"),

    # Filmovi
    path("films/", FilmListView.as_view(), name="film_list"),
    path("film/add/", FilmCreateView.as_view(), name="film_add"),
    path("film/<int:pk>/", FilmDetailView.as_view(), name="film_detail"),
    path("film/<int:pk>/edit/", FilmUpdateView.as_view(), name="film_edit"),
    path("film/<int:pk>/delete/", FilmDeleteView.as_view(), name="film_delete"),

    #Redateljji
    path("directors/", DirectorListView.as_view(), name="director_list"),
    path("director/add/", DirectorCreateView.as_view(), name="director_add"),
    path("director/<int:pk>/edit/", DirectorUpdateView.as_view(), name="director_edit"),
    path("director/<int:pk>/delete/", DirectorDeleteView.as_view(), name="director_delete"),
]