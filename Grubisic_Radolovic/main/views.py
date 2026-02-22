from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import RegisterForm, FilmForm, DirectorForm, ReviewForm
from django.contrib.auth import login
from .models import Director, Film, Review
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied


# Create your views here.

# REGISTRACIJA

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("main:home")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.success_url)

# NASLOVNICA
class HomeView(ListView):
    model = Film
    template_name = "main/home.html"
    context_object_name = "films"

    def get_queryset(self):
        queryset = Film.objects.all()

        query = self.request.GET.get("q")
        genre = self.request.GET.get("genre")
        director = self.request.GET.get("director")

        if query:
            queryset = queryset.filter(title__icontains=query)

        if genre:
            queryset = queryset.filter(genre=genre)

        if director:
            queryset = queryset.filter(director__id=director)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["genres"] = Film.GENRE_CHOICES 
        context["directors"] = Director.objects.all()
        return context
    
# REDATELJI

# Prikaz - svi redatelji
class DirectorListView(ListView):
    model = Director
    template_name = "main/director_list.html"
    context_object_name = "directors"

# Dodavanje redatelja
class DirectorCreateView(LoginRequiredMixin, CreateView):
    model = Director
    form_class = DirectorForm
    template_name = "main/director_form.html"
    success_url = reverse_lazy("main:director_list")

# Ažuriranje redatelja
class DirectorUpdateView(LoginRequiredMixin, UpdateView):
    model = Director
    form_class = DirectorForm
    template_name = "main/director_form.html"
    success_url = reverse_lazy("main:director_list")

# Brisanje redatelja
class DirectorDeleteView(LoginRequiredMixin, DeleteView):
    model = Director
    success_url = reverse_lazy("main:director_list")

    def dispatch(self, request, *args, **kwargs):
        director = self.get_object()
        director.delete()
        return redirect(self.success_url)


# FILMOVI
# Prikaz - svi filmovi
class FilmListView(ListView):
    model = Film
    template_name = "main/film_list.html"
    context_object_name = "films"

# Prikaz - detalji o filmu
class FilmDetailView(DetailView):
    model = Film
    template_name = "main/film_detail.html"
    context_object_name = "film"

# Dodavanje filma
class FilmCreateView(LoginRequiredMixin, CreateView):
    model = Film
    form_class = FilmForm
    template_name = "main/film_form.html"
    success_url = reverse_lazy("main:film_list")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

# Ažuriranje filma
class FilmUpdateView(LoginRequiredMixin, UpdateView):
    model = Film
    form_class = FilmForm
    template_name = "main/film_form.html"
    success_url = reverse_lazy("main:film_list")

    def dispatch(self, request, *args, **kwargs):
        film = self.get_object()
        return super().dispatch(request, *args, **kwargs)


class FilmDeleteView(LoginRequiredMixin, DeleteView):
    model = Film
    success_url = reverse_lazy("main:film_list")

    def dispatch(self, request, *args, **kwargs):
        film = self.get_object()
        film.delete()
        return redirect(self.success_url)
    
# RECENZIJE

# Dodavanje recenzije
class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "main/review_form.html"

    def form_valid(self, form):
        film = get_object_or_404(Film, pk=self.kwargs["pk"])
        form.instance.film = film
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("main:film_detail", kwargs={"pk": self.kwargs["pk"]})


# Ažuriranje recenzije
class ReviewUpdateView(LoginRequiredMixin, UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = "main/review_form.html"

    def dispatch(self, request, *args, **kwargs):
        review = self.get_object()
        if review.user != request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
         return reverse_lazy("main:user_reviews")


# Brisanje recenzije
class ReviewDeleteView(LoginRequiredMixin, DeleteView):
    model = Review

    def dispatch(self, request, *args, **kwargs):
        review = self.get_object()
        if review.user != request.user:
            raise PermissionDenied

        review.delete()
        return redirect("main:user_reviews")


# Prikaz korisničkih recenzija
class UserReviewsListView(LoginRequiredMixin, ListView):
    model = Review
    template_name = "main/user_reviews.html"
    context_object_name = "reviews"

    def get_queryset(self):
        return Review.objects.filter(user=self.request.user)
