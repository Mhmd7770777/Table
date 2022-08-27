from rest_framework import serializers

from artists.models import Artist, Gender, Country


class ArtistSerializer(serializers.ModelSerializer):
    gender = serializers.PrimaryKeyRelatedField(
        queryset=Gender.objects.all(), many=False
    )

    country = serializers.PrimaryKeyRelatedField(
        queryset=Country.objects.all(), many=False
    )

    class Meta:
        fields = ("pk", "name", "age", "gender", "country")
        model = Artist
        depth = 1
