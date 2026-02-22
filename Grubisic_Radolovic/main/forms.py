from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Film, Director, Review

# Registracija
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

#Film
class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ["title", "description", "release_year", "genre", "director"]

        widgets = {
            "description": forms.Textarea(attrs={"rows": 4}),
        }

#Redatelj
class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = ["name", "birth_year"]
        
# Recenzija
class ReviewForm(forms.ModelForm):
    RATING_CHOICES = [(i, i) for i in range(1, 6)]

    rating = forms.ChoiceField(choices=RATING_CHOICES)

    class Meta:
        model = Review
        fields = ["rating", "comment"]

    def clean_rating(self):
        rating = int(self.cleaned_data["rating"])
        if rating < 1 or rating > 5:
            raise forms.ValidationError("Ocjena mora biti između 1 i 5.")
        return rating
