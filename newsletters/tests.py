from django.contrib.auth.models import User
from rest_framework.test import APITestCase

from newsletters.models import Newsletters
from tags.models import Tags


class TestNewletter(APITestCase):

    def setUp(self):
        self.host = 'http://127.0.0.1:8000'
        self.user = User.objects.create(
            username='alan',
            email='alan@gmail.com',
            first_name='hjgfhg',
            last_name='jhgvjhgv',
            password='edgar124',
        )
        self.tag = Tags.objects.create(
            name='Hola',
            slug='tal',
            create_at='2012-04-25'
        )

        self.newletter = Newsletters.objects.create(
            name='delincuencia',
            description='delincuencia',
            image='tal',
            target='1',
            frequency='diario',
            votes='65',
            create_at='2012-04-25'
        )
        self.newletter.members.add(1)
        self.newletter.tags.add(1)

    def test_get_newsletter(self):
        response = self.client.get(f'{self.host}/newsletters/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_post_newsletter(self):
        data = {
            'name': 'casas',
            'description': 'hogares',
            'image': 'home',
            'target': '1',
            'frequency': 'all',
            'votes': '454',
            'create_at': '2012-04-30',
            'user': '1',
            'members': [1],
            'tags': [1]
        }
        response = self.client.post(f'{self.host}/newsletters/', data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Newsletters.objects.all().count(), 2)

    def test_put_newsletter(self):
        data = {
            'name': 'casas2',
            'description': 'hogares',
            'image': 'home2',
            'target': '1',
            'frequency': 'all',
            'votes': '44',
            'create_at': '2012-04-30',
            'user': '1',
            'members': [1],
            'tags': [1]
        }
        response = self.client.put(f'{self.host}/newsletters/1/', data)
        self.assertEqual(response.status_code, 200, response.data)

    def test_delete_newsletter(self):

        response = self.client.delete(f'{self.host}/newsletters/1/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Newsletters.objects.all().count(), 0)
