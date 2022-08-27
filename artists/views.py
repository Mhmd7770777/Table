from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, parser_classes

from artists.models import Artist, Gender, Country
from artists.serializers import ArtistSerializer

# Create your views here.
@csrf_exempt
@api_view(["GET", "POST"])
@parser_classes([JSONParser])
def artists_list(request):
    if request.method == "GET":
        artists = Artist.objects.all()
        serializer = ArtistSerializer(artists, many=True)

        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        serializer = ArtistSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False, status=201)

        return JsonResponse(serializer.errors, safe=False, status=400)
