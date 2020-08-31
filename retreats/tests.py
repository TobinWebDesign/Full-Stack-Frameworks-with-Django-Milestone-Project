from django.test import TestCase, Client
from django.urls import reverse, resolve

# Create your tests here.

from retreats.models import Category


class TestCategory(TestCase):
    def setUp(self):
        Category.objects.create(name='catone', friendly_name='First Category')
        Category.objects.create(name='cattwo', friendly_name='cattwo')

    def test_get_friendly_name(self):
        catone = Category.objects.get(name='catone')
        cattwo = Category.objects.get(name='cattwo')
        self.assertEqual(catone.get_friendly_name(), 'First Category')
        self.assertEqual(cattwo.get_friendly_name(), 'cattwo')

class TestViews(TestCase):
#test_main_view_GET test is displayed on the main url in main_tour_folder
    def test_home_page(self):
        page = self.client.get('/')
        self.assertEquals(page.status_code, 200)
        self.assertTemplateUsed(page, 'base.html')

    def test_retreats_GET(self):
        client = Client()
        response = client.get(reverse('retreats'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'retreats/retreats.html')