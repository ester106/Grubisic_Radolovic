from django.test import SimpleTestCase
from django.urls import reverse, resolve
from main.views import (
    HomeView,
    FilmListView, FilmCreateView, FilmDetailView, FilmUpdateView, FilmDeleteView,
    DirectorListView, DirectorCreateView, DirectorUpdateView, DirectorDeleteView,
    ReviewCreateView, ReviewUpdateView, ReviewDeleteView,
    UserReviewsListView,
    RegisterView
)


class TestUrls(SimpleTestCase):

    # Home
    def test_home_url(self):
        url = reverse("main:home")
        self.assertEqual(resolve(url).func.view_class, HomeView)

    # Registracija
    def test_register_url(self):
        url = reverse("main:register")
        self.assertEqual(resolve(url).func.view_class, RegisterView)

    # Filmovi
    def test_film_list_url(self):
        url = reverse("main:film_list")
        self.assertEqual(resolve(url).func.view_class, FilmListView)

    def test_film_add_url(self):
        url = reverse("main:film_add")
        self.assertEqual(resolve(url).func.view_class, FilmCreateView)

    def test_film_detail_url(self):
        url = reverse("main:film_detail", args=[1])
        self.assertEqual(resolve(url).func.view_class, FilmDetailView)

    def test_film_edit_url(self):
        url = reverse("main:film_edit", args=[1])
        self.assertEqual(resolve(url).func.view_class, FilmUpdateView)

    def test_film_delete_url(self):
        url = reverse("main:film_delete", args=[1])
        self.assertEqual(resolve(url).func.view_class, FilmDeleteView)

    # Redatelji
    def test_director_list_url(self):
        url = reverse("main:director_list")
        self.assertEqual(resolve(url).func.view_class, DirectorListView)

    def test_director_add_url(self):
        url = reverse("main:director_add")
        self.assertEqual(resolve(url).func.view_class, DirectorCreateView)

    def test_director_edit_url(self):
        url = reverse("main:director_edit", args=[1])
        self.assertEqual(resolve(url).func.view_class, DirectorUpdateView)

    def test_director_delete_url(self):
        url = reverse("main:director_delete", args=[1])
        self.assertEqual(resolve(url).func.view_class, DirectorDeleteView)

    # Recenzije
    def test_review_add_url(self):
        url = reverse("main:review_add", args=[1])
        self.assertEqual(resolve(url).func.view_class, ReviewCreateView)

    def test_review_edit_url(self):
        url = reverse("main:review_edit", args=[1])
        self.assertEqual(resolve(url).func.view_class, ReviewUpdateView)

    def test_review_delete_url(self):
        url = reverse("main:review_delete", args=[1])
        self.assertEqual(resolve(url).func.view_class, ReviewDeleteView)

    def test_user_reviews_url(self):
        url = reverse("main:user_reviews")
        self.assertEqual(resolve(url).func.view_class, UserReviewsListView)