


from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.authtoken import views as token_auth_views
from .views import UserCreateOrListView #, ObtainAuthToken

app_name = 'users'

urlpatterns = [
    #path('api-token-auth/', obtain_auth_token, name='get_token'),
    path('auth/', obtain_auth_token, name='get_token'),
    path('createuser/', UserCreateOrListView.as_view(), name='user_create_or_list'),
]
