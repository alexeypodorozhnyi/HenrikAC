from django.urls import path

from . import views

app_name = 'blogposts'
urlpatterns = [
    path('comment/delete/<int:pk>/', views.CommentDeleteView.as_view(), name='comment_delete'),
    path('<slug:slug>/', views.BlogPostDetailView.as_view(), name='detail'),
    path('', views.BlogPostListView.as_view(), name='list'),
]