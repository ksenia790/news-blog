from django.urls import path
#from rest_framework.authtoken.views import obtain_auth_token
#from rest_framework.authtoken import views as token_auth_views
from .views import UserCreateOrListView, GetToken

app_name = 'users'

urlpatterns = [
    path('auth/<int:id>/', GetToken.as_view(), name='get_token'),
    path('createuser/', UserCreateOrListView.as_view(), name='user_create_or_list'),
]
