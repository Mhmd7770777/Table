from rest_framework import serializers

from artists.models import Artist

class UserPublicSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True)
    this_is_not_real = serializers.CharField(read_only=True)
    id = serializers.IntegerField(read_only=True)


class ArtistSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(source='user',read_only=True)
    class Meta:
        fields = ("pk","owner", "name", "age", "gender", "country")
        model = Artist
        depth = 1
