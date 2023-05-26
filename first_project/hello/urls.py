# Importar una biblioteca administradora de rutas

from django.urls import path

# Importando vistas

from . import views

# Declarando las rutas validas 

urlpatterns = [
    # GET /hello/
    path("", views.index, name="index"),
    # GET /hello/author
    path("author/", views.author, name="author"),
]