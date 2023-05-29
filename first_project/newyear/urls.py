from django.urls import path
# Importando views del directorio actual
from . import views

urlpatterns = [
    path("", views.index, name="index"),
]