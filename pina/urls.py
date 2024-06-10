from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("portfolio", views.portfolio, name="portfolio"),
    path("crie", views.crie, name="crie"),

    path("crie_form", views.crie_form, name="crie_form")
]