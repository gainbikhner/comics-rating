from http import HTTPStatus

from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.serializers import ComicSerializer, RatingSerializer
from models.models import Comic, Rating


@api_view()
def get_rating(request, comic_id):
    '''Функция получения среднего рейтинга комикса.'''
    comic = Comic.objects.get(id=comic_id)
    serializer = ComicSerializer(comic)
    return Response(serializer.data, status=HTTPStatus.OK)


@api_view(['POST'])
def post_rating(request):
    '''Функция создания оценки комикса.'''
    try:
        rating = Rating.objects.get(
            comic_id=request.data['comic_id'],
            user_id=request.data['user_id']
        )
    except Rating.DoesNotExist:
        serializer = RatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTPStatus.CREATED)
        return Response(serializer.errors, status=HTTPStatus.BAD_REQUEST)

    serializer = RatingSerializer(rating, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=HTTPStatus.ACCEPTED)
    return Response(serializer.errors, status=HTTPStatus.BAD_REQUEST)
