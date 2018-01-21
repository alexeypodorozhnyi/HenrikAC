from django.urls import path

from . import views

app_name = 'blogposts'
urlpatterns = [
    path('', views.BlogPostListView.as_view(), name='list'),
]