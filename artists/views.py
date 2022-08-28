from rest_framework import generics

from artists.models import Artist
from artists.serializers import ArtistSerializer


class ArtistsView(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class ArtistFilterView(generics.ListAPIView):

    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

    def get_queryset(self, *args, **kwargs):
        age = self.request.GET.get("age")
        country = self.request.GET.get("country")
        gender = self.request.GET.get("gender")
        results = Artist.objects.all()

        if age is not None:
            results = results.filter(age=age)
        if country is not None:
            results = results.filter(country=country)
        if gender is not None:
            results = results.filter(gender=gender.capitalize())

        return results


class ArtistSearchView(generics.ListAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

    def get_queryset(self, *args, **kwargs):
        qset = super().get_queryset(*args, **kwargs)
        search_name = self.request.GET.get("name")

        if search_name is not None:
            return qset.filter(name__icontains=search_name)
        else:
            return qset
