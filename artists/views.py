from django.shortcuts import render

from rest_framework import viewsets

from artists.serializers import ArtistSerializer
from artists.models import Artist

# Create your views here.

class ArtistViewSet(viewsets.ModelViewSet):
   queryset = Artist.objects.all()
   serializer_class = ArtistSerializer