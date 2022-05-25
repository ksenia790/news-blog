from django.urls import path
from users.views import register, user_login

app_name = 'news'

urlpatterns=[
    path('', register, name="register"),
    path('login/', user_login, name="user_login"),
]