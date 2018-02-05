from django.test import TestCase
from django.urls import reverse

from . import models


class PortfolioProjectModelTest(TestCase):
    """Testing PortfolioProject model"""
    def test_portfolio_project_creation(self):
        project = models.PortfolioProject.objects.create(
            title='My first project',
            description='A random description for my first project',
            photo_file_name='my-first-project.jpg',
            url='http://www.my-project.com',
            order=1
        )
        self.assertTrue(models.PortfolioProject.objects.filter(title='My first project').exists())


class PortfolioProjectViewTest(TestCase):
    """Testing PortfolioProject views, urls and templates"""
    def setUp(self):
        self.project = models.PortfolioProject.objects.create(
            title='My first project',
            description='A random description for my first project',
            photo_file_name='my-first-project.jpg',
            url='http://www.my-project.com',
            order=1
        )

    def test_portfolio_list_view(self):
        """Testing PortFolioProject listview, url and template"""
        resp = self.client.get(reverse('portfolio:list'))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'My first project')
        self.assertTemplateUsed(resp, 'portfolioprojects/portfolioproject_list.html')
