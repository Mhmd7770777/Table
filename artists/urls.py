from django.urls import path
from artists import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path("", views.ArtistsView.as_view()),
    path("filter/", views.ArtistFilterView.as_view()),
    path("search/", views.ArtistSearchView.as_view()),
    path("sort/<type>", views.ArtistSortView.as_view()),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
]
