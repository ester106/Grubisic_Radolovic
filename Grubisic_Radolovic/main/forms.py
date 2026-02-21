from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Film, Director

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
