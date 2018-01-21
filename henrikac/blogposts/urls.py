from django.urls import path

from . import views

app_name = 'blogposts'
urlpatterns = [
    path('<int:pk>/', views.BlogPostDetailView.as_view(), name='detail'),
    path('', views.BlogPostListView.as_view(), name='list'),
]