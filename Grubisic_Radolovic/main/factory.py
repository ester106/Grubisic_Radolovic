import random
import factory
from factory.django import DjangoModelFactory
from django.contrib.auth.models import User
from django.utils import timezone

from main.models import Director, Film, Review


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ("username",)

    username = factory.Faker("user_name")
    email = factory.Faker("email")
    password = factory.PostGenerationMethodCall("set_password", "test1234")


class DirectorFactory(DjangoModelFactory):
    class Meta:
        model = Director

    name = factory.Faker("name")
    birth_year = factory.Faker("year")


class FilmFactory(DjangoModelFactory):
    class Meta:
        model = Film

    title = factory.Faker("sentence", nb_words=3)
    description = factory.Faker("text", max_nb_chars=300)
    release_year = factory.Faker("year")
    genre = factory.Iterator([g[0] for g in Film.GENRE_CHOICES])

    director = factory.SubFactory(DirectorFactory)
    created_by = factory.SubFactory(UserFactory)
    created_at = factory.LazyFunction(timezone.now)


class ReviewFactory(DjangoModelFactory):
    class Meta:
        model = Review

    film = factory.SubFactory(FilmFactory)
    user = factory.SubFactory(UserFactory)
    rating = factory.Faker("random_int", min=1, max=5)
    comment = factory.Faker("sentence")
    created_at = factory.LazyFunction(timezone.now)