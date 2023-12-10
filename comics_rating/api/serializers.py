from rest_framework.serializers import ModelSerializer

from models.models import Comic, Rating


class ComicSerializer(ModelSerializer):
    '''Сериализатор для модели Comic.'''
    class Meta:
        model = Comic
        fields = ('rating',)


class RatingSerializer(ModelSerializer):
    '''Сериализатор для модели Rating.'''
    class Meta:
        model = Rating
        fields = '__all__'
