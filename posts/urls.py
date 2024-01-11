from django.urls import path
from .views import Main

urlpatterns = [
    path('', Main.as_view()),  # .as_view()를 사용하여 뷰를 지정
]