from django.urls import path
from users.views import register, user_login, user_logout

app_name = 'news'

urlpatterns=[
    path('register/', register, name="register"),
    path('login/', user_login, name="user_login"),
    path('logout/', user_logout, name='logout'),
]