from django.urls import path

from api.views import get_rating, post_rating


app_name = 'api'

urlpatterns = [
    path('comics/<int:comic_id>/rating/', get_rating),
    path('ratings/', post_rating),
]
