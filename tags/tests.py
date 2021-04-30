from rest_framework.test import APITestCase
from tags.models import Tags


class TestTags(APITestCase):

    def setUp(self):
        self.host = 'http://127.0.0.1:8000/'

        self.tag = Tags.objects.create(
            name='Hola',
            slug='tal'
        )

    def test_get_tag(self):
        response = self.client.get(f'{self.host}tags/')
        self.assertEqual(response.status_code, 200)
        print(response.data)
