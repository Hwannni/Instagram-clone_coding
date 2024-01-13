from django.contrib import admin
from django.urls import path, include

from posts import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('posts.urls')),
    #path("", include('content.urls')),
    path("", include('user.urls')),
]
