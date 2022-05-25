from django.urls import path
from . import views

app_name = 'news'

urlpatterns=[
    path('news/', views.news_list, name="news"),
    path('deletenews/', views.delete_all_news, name="delete_news"),
]