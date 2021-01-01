from random import randint

from django.http import JsonResponse
from django.shortcuts import render

from .models import Tweet
from .forms import TweetForm


def home_page(request, *args, **kwargs):
    return render(request, "pages/home.html", context={}, status=200)


def tweet_create_view(request, *args, **kwargs):
    form = TweetForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        form = TweetForm()

    return render(request, "components/form.html", context={"form": form})


def tweet_list_view(request, *args, **kwargs):
    qs = Tweet.objects.all()
    tweets_list = [
        {
            "id": x.id,
            "content": x.content,
            "likes": randint(0, 740)
        } for x in qs
    ]
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
