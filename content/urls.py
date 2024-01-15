from django.urls import path
from .views import UploadFeed
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('upload', UploadFeed.as_view())
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)