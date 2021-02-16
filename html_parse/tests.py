from django.test import TestCase

# Create your tests here.
from django.urls import reverse


class ParseTest(TestCase):
    url = reverse('html_parse:parser')

    def test_url(self):
        response = self.client.get(self.url, {'url': 'https://www.defacto.com.tr/kiz-bebek-sevimli-kopek-baskil-pijam-takimi-1825969'})
        self.assertEqual(200,response.status_code)