from django.urls import path

from . import views

app_name = 'portfolioprojects'
urlpatterns = [
    path('', views.PortfolioProjectListView.as_view(), name='list'),
]
