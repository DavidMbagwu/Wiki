from django.urls import include, path
from . import views


urlpatterns = [
    path("new_title/", views.new_title, name="new_title"),
    path("new_content/", views.new_content, name="new_content"),
    path("random/", views.randome, name="random"),
    path("new/", views.new, name="new"),
    path("search/", views.search, name="search"),
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("edit/", views.edit, name="edit"),
    path("wiki/CSS", views.entry, name="css"),
    path("wiki/Django", views.entry, name="Django"),
    path("wiki/Git", views.entry, name="Git"),
    path("wiki/HTML", views.entry, name="HTML"),
    path("wiki/Python", views.entry, name="Python")
]
