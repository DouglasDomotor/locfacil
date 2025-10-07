from django.test import TestCase
from django.urls import reverse

class CoreUrlsTestCase(TestCase):
    def test_index_status_code(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<h1>Bem vindo à minha primeira página, do Locfacil!!!</h1>')
        