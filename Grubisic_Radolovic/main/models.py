from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Director(models.Model):
    name = models.CharField(max_length=100)
    birth_year = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class Film(models.Model):
    GENRE_CHOICES = [
        ('ACTION', 'Action'),
        ('DRAMA', 'Drama'),
        ('COMEDY', 'Comedy'),
        ('THRILLER', 'Thriller'),
        ('HORROR', 'Horror'),
        ('ROMANCE', 'Romance'),
        ('SCIFI', 'Sci-Fi'),
        ('OTHER', 'Other'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    release_year = models.IntegerField()
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES)

    director = models.ForeignKey(
        Director,
        on_delete=models.SET_NULL,
        null=True,
        related_name='films'
    )

    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='created_films'
    )

    def __str__(self):
        return f"{self.title} ({self.release_year})"


class Review(models.Model):
    film = models.ForeignKey(
        Film,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews'
    )

    rating = models.IntegerField()
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} - {self.film.title} ({self.rating}/5)"
