from django.urls import path
from .views import Main, UploadFeed
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', Main.as_view()),  # .as_view()를 사용하여 뷰를 지정
    path('content/upload', UploadFeed.as_view())
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)