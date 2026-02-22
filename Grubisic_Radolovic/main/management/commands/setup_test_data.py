import random
from django.db import transaction
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from main.models import Director, Film, Review
from main.factory import (
    UserFactory,
    DirectorFactory,
    FilmFactory,
    ReviewFactory
)

NUM_USERS = 5
NUM_DIRECTORS = 10
NUM_FILMS = 20
NUM_REVIEWS = 50


class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")

        Review.objects.all().delete()
        Film.objects.all().delete()
        Director.objects.all().delete()
        User.objects.filter(is_superuser=False).delete()

        self.stdout.write("Creating new data...")

        users = [UserFactory() for _ in range(NUM_USERS)]
        directors = [DirectorFactory() for _ in range(NUM_DIRECTORS)]
        films = []

        for _ in range(NUM_FILMS):
            film = FilmFactory(
                director=random.choice(directors),
                created_by=random.choice(users)
            )
            films.append(film)

        for _ in range(NUM_REVIEWS):
            ReviewFactory(
                film=random.choice(films),
                user=random.choice(users)
            )

        self.stdout.write("Test data created!")