from django.urls import path

from . import views

app_name = 'blogposts'
urlpatterns = [
    path('<slug>/', views.BlogPostDetailView.as_view(), name='detail'),
    path('', views.BlogPostListView.as_view(), name='list'),
]