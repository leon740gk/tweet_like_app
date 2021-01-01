from random import randint
from django.conf import settings

from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.utils.http import is_safe_url

from .models import Tweet
from .forms import TweetForm

ALLOWED_HOSTS = settings.ALLOWED_HOSTS


def home_page(request, *args, **kwargs):
    return render(request, "pages/home.html", context={}, status=200)


def tweet_create_view(request, *args, **kwargs):
    form = TweetForm(request.POST or None)
    next_url = request.POST.get("next")
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        if next_url and is_safe_url(next_url, ALLOWED_HOSTS):
            return redirect(next_url)
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
