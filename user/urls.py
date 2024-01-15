from django.urls import path
from .views import Login, Join

app_name = 'user'

urlpatterns = [
    path('login', Login.as_view(), name='login'),
    path('join', Join.as_view(), name='join'),
]