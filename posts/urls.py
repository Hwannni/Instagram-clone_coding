from django.urls import path, include
from .views import Main
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', Main.as_view()),  # .as_view()를 사용하여 뷰를 지정
    path('content/', include('content.urls')),
    path('user/', include('user.urls'))
]