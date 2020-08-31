from django.test import TestCase, Client
from django.urls import reverse, resolve

# Create your tests here.

from classes.models import Class, Level


class TestLevel(TestCase):
    def setUp(self):
        Level.objects.create(name='Advanced', friendly_name='Advanced')
        Level.objects.create(name='Intermediate', friendly_name='Intermediate')

    def test_get_friendly_name(self):
        catone = Level.objects.get(name='Advanced')
        cattwo = Level.objects.get(name='Intermediate')
        self.assertEqual(catone.get_friendly_name(), 'Advanced')
        self.assertEqual(cattwo.get_friendly_name(), 'Intermediate')

class TestViews(TestCase):
#test_main_view_GET test is displayed on the main url in main_tour_folder
    def test_home_page(self):
        page = self.client.get('/')
        self.assertEquals(page.status_code, 200)
        self.assertTemplateUsed(page, 'base.html')

    def test_classes_GET(self):
        client = Client()
        response = client.get(reverse('classes'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'classes/classes.html')