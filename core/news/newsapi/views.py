from rest_framework.generics import ListAPIView, CreateAPIView
from .serializers import NewsListSerializer
from news.models import Post
#from rest_framework.permissions import IsAuthenticated
#from users.usersapi.customauth import CustomAuthentication


class NewsListAPIView(ListAPIView, CreateAPIView):
    #authentication_classes = [CustomAuthentication]
    #permission_classes = (IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = NewsListSerializer
