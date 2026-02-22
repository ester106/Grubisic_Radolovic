from django.test import TestCase
from django.contrib.auth.models import User
from main.models import Director, Film, Review


class TestModels(TestCase):

    def setUp(self):
        #user
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123"
        )

        #redatelj
        self.director = Director.objects.create(
            name="Christopher Nolan",
            birth_year=1970
        )

        #film
        self.film = Film.objects.create(
            title="Inception",
            description="A mind-bending thriller",
            release_year=2010,
            genre="SCIFI",
            director=self.director,
            created_by=self.user
        )

        #recenzija
        self.review = Review.objects.create(
            film=self.film,
            user=self.user,
            rating=5,
            comment="Amazing movie!"
        )

    def test_director_fields(self):
        self.assertEqual(self.director.name, "Christopher Nolan")
        self.assertEqual(self.director.birth_year, 1970)
        self.assertEqual(str(self.director), "Christopher Nolan")

    def test_film_fields(self):
        self.assertEqual(self.film.title, "Inception")
        self.assertEqual(self.film.release_year, 2010)
        self.assertEqual(self.film.genre, "SCIFI")
        self.assertEqual(self.film.director, self.director)
        self.assertEqual(self.film.created_by, self.user)
        self.assertEqual(str(self.film), "Inception")

    def test_review_fields(self):
        self.assertEqual(self.review.film, self.film)
        self.assertEqual(self.review.user, self.user)
        self.assertEqual(self.review.rating, 5)
        self.assertEqual(self.review.comment, "Amazing movie!")
        self.assertEqual(str(self.review), "testuser - Inception")