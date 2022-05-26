from django.urls import path
from .views import NewsListAPIView

app_name = 'news'

urlpatterns = [
    path('listnews/', NewsListAPIView.as_view(), name="post_list"),
]
