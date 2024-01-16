from django.urls import path, include
from .views import Main
from django.conf import settings
from django.conf.urls.static import static

app_name = "posts"

urlpatterns = [
    path('', Main.as_view(), name="main"),  
    path('content/', include('content.urls')),
    path('user/', include('user.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)