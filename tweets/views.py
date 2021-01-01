from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from .models import Tweet


def home_page(request, *args, **kwargs):
    return render(request, "pages/home.html", context={}, status=200)

def tweet_list_view(request, *args, **kwargs):
    qs = Tweet.objects.all()
    tweets_list = [{"id": x.id, "content": x.content} for x in qs]
    data = {
        "response": tweets_list
    }

    return JsonResponse(data=data)

def tweet_detail_view(request, tweet_id, *args, **kwargs):
    tweet = Tweet.objects.get(id=tweet_id)
    data = {
        "id": tweet.id,
        "content": tweet.content,
    }
    return JsonResponse(data=data)
