from django.urls import path
from artists import views

urlpatterns = [
    path("", views.ArtistsView.as_view()),
    path("filter/", views.ArtistFilterView.as_view()),
    path("search/", views.ArtistSearchView.as_view()),
    path("sort/<type>", views.ArtistSortView.as_view()),
]
