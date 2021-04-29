from rest_framework.test import APITestCase

from newsletters.models import Newsletters
from tags.models import Tags


class NewletterTests(APITestCase):

    def setUp(self):
        self.host = 'http://127.0.0.1:8000/'

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
            create_at='2012-04-25',
            User=1,
            members=1,
            tags=1
        )

    def test_get_newsletter(self):
        response = self.client.get(f'{self.host}/newsletters/')
        self.assertEqual(response.status_code, 200)
