from django.test import TestCase
from django.urls import reverse


class HomeViewTest(TestCase):
    """Testing home view, url and template"""
    def test_home_view(self):
        """Testing home view, url and template"""
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Who am I?')
        self.assertTemplateUsed(resp, 'index.html')
