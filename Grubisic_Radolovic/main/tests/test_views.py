from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

from main.models import Director, Film, Review


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()

        # Kreiranje usera
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123"
        )

        #Kreiranje redatelja
        self.director = Director.objects.create(
            name="Christopher Nolan"
        )

        #Kreiranje filma
        self.film = Film.objects.create(
            title="Inception",
            genre="SCIFI",
            director=self.director,
            created_by=self.user,
            release_year=2010,
            description="A mind-bending thriller"
        )

        #urlovi
        self.home_url = reverse("main:home")
        self.film_list_url = reverse("main:film_list")
        self.film_detail_url = reverse("main:film_detail", args=[self.film.id])
        self.review_add_url = reverse("main:review_add", args=[self.film.id])
        self.user_reviews_url = reverse("main:user_reviews")

    #HOME
    def test_home_GET(self):
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "main/home.html")

    #FILM LIST
    def test_film_list_GET(self):
        response = self.client.get(self.film_list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "main/film_list.html")

    #FILM DETAIL
    def test_film_detail_GET(self):
        response = self.client.get(self.film_detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "main/film_detail.html")

    #REVIEW ADD
    def test_review_add_requires_login(self):
        response = self.client.get(self.review_add_url)
        self.assertEqual(response.status_code, 302)

    def test_review_add_logged_in_GET(self):
        self.client.login(username="testuser", password="testpass123")
        response = self.client.get(self.review_add_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "main/review_form.html")

    def test_review_add_logged_in_POST(self):
        self.client.login(username="testuser", password="testpass123")
        response = self.client.post(self.review_add_url, {
            "rating": 5,
            "comment": "Amazing movie!"
        })
        self.assertEqual(response.status_code, 302) 
        self.assertTrue(Review.objects.filter(film=self.film, user=self.user).exists())

    #USER REVIEWS
    def test_user_reviews_requires_login(self):
        response = self.client.get(self.user_reviews_url)
        self.assertEqual(response.status_code, 302) 

    def test_user_reviews_logged_in(self):
        self.client.login(username="testuser", password="testpass123")
        response = self.client.get(self.user_reviews_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "main/user_reviews.html")