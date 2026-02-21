from django.urls import path
from .views import *

app_name = "main"

urlpatterns = [
    # Registracija
    path("register/", RegisterView.as_view(), name="register"),
]