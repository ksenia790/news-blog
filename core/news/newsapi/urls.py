from django.urls import path
from .views import PostListAPIView

app_name = 'post'

urlpatterns = [
    path('listnews/', PostListAPIView.as_view(), name="post_list"),
]
