from django.views import generic

from . import models


class PortfolioProjectListView(generic.ListView):
    model = models.PortfolioProject
