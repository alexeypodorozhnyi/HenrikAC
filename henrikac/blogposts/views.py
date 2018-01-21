from django.shortcuts import render
from django.views import generic

from . import models


class BlogPostListView(generic.ListView):
    model = models.BlogPost


class BlogPostDetailView(generic.DetailView):
    model = models.BlogPost
