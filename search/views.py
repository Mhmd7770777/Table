
from rest_framework import generics, mixins

from artists.models import Artist
from artists.serializers import ArtistSerializer

from artists.models import COUNTRY_CHOICES

# Create your views here.
class ArtistFilterView(generics.ListAPIView):

    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

    def get_queryset(self, *args, **kwargs):
        age = self.request.GET.get('age')
        country = self.request.GET.get('country')
        gender = self.request.GET.get('gender')
        results = Artist.objects.all()
        if age is not None:
            results1 = results.filter(age=age)  
            print(results)  
        else:       
            results1 = results
        if country is not None:
            print(country)
            results2 = results1.filter(country=country.capitalize())
        else:
            results2= results1  
        if gender is not None:
            print(gender)
            results3 = results2.filter(gender=gender.capitalize()) 
        else:
            results3= results2 
        return results3

class ArtistSearchView(generics.ListAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        q = self.request.GET.get('q')
        results = Artist.objects.none()
        if q is not None:
            results = qs.filter(name__icontains=q)
        return results
        
