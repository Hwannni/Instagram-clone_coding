from django.contrib import admin
from django.urls import path, include

from posts import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('posts.urls')),
    path("common/", include('user.urls')),
    #path("urls/", include('user.urls')),
]
