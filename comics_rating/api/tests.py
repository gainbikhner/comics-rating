from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.test import Client, TestCase

from models.models import Comic


User = get_user_model()


class RatingTestCase(TestCase):
    def setUp(self):
        self.user = Client()
        self.comic = Comic.objects.create(
            title="Test_title",
            author="Test_author"
        )
        User.objects.create_user(username='Test_user')
        User.objects.create_user(username='Test_user2')

    def test_create_and_update_rating(self):
        '''Тест на создание оценки и обновление рейтинга комикса.'''
        response = self.user.post(
            '/api/ratings/',
            {'comic_id': 1, 'user_id': 1, 'VALUE': 5}
        )
        self.assertEqual(response.status_code, HTTPStatus.CREATED)
        self.assertEqual(
            response.json(),
            {"id": 1, "VALUE": 5, "comic_id": 1, "user_id": 1}
        )
        self.assertEqual(self.comic.rating, 5)

        response = self.user.post(
            '/api/ratings/',
            {'comic_id': 1, 'user_id': 1, 'VALUE': 1}
        )
        self.assertEqual(response.status_code, HTTPStatus.ACCEPTED)
        self.assertEqual(
            response.json(),
            {"id": 1, "VALUE": 1, "comic_id": 1, "user_id": 1}
        )
        self.assertEqual(self.comic.rating, 1)

    def test_get_avg_rating(self):
        '''Тест на получение среднего рейтинга комикса.'''
        self.user.post(
            '/api/ratings/',
            {'comic_id': 1, 'user_id': 1, 'VALUE': 5}
        )

        response = self.user.get('/api/comics/1/rating/')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.json(), {'rating': 5.0})

        self.user.post(
            '/api/ratings/',
            {'comic_id': 1, 'user_id': 2, 'VALUE': 1}
        )

        response = self.user.get('/api/comics/1/rating/')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.json(), {'rating': 3.0})
