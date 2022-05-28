from django.shortcuts import render, get_object_or_404, redirect
from newsapi.newsapi_client import NewsApiClient
from .models import Post
from django.contrib.auth.decorators import login_required

API_KEY='4d104adb88384256ad43133df6d3867e' #https://newsapi.org/register

@login_required
def news_list(request):
    '''
    Returns all news posts.
    '''
    newsApi = NewsApiClient(API_KEY)
    headLines = newsApi.get_top_headlines(sources='ign, cnn')
    articles = headLines['articles']

    for i in range(len(articles)):
        article = articles[i]
        post = Post()
        post.title = article['title']
        post.content = article['description']
        post.date = article['publishedAt']
        post.url = article['url']
        post.image = article['urlToImage']
        post.save()
       
    posts = Post.objects.all()
    return render(request,'news.html',{'posts':posts,})

@login_required
def delete_all_news(request):
    Post.objects.all().delete()
    return render(request, "deletenews.html")
