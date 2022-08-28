from rest_framework import serializers

from artists.models import Artist


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("pk", "name", "age", "gender", "country")
        model = Artist
        depth = 1
