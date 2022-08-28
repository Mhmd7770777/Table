from django.urls import path
from search import views

urlpatterns = [
    path("", views.ArtistSearchView.as_view()),
    path("filter", views.ArtistFilterView.as_view()),
]
