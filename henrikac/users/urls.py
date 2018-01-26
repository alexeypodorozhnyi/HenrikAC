from django.urls import include, path

from . import views

app_name = 'users'
urlpatterns = [
    path('login/', views.MyLoginView.as_view(), name='login'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('', include('django.contrib.auth.urls')),
]
