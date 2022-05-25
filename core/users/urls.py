from django.urls import path
from users.views import register

app_name = 'news'

urlpatterns=[
    path('', register, name="register"),
]