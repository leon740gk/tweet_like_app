from django.conf import settings
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Tweet
from .serializers import TweetActionSerializer, TweetSerializer

ALLOWED_HOSTS = settings.ALLOWED_HOSTS


def home_page(request, *args, **kwargs):
    return render(request, "pages/home.html", context={}, status=200)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def tweet_create_view(request, *args, **kwargs):
    serializer = TweetSerializer(data=request.POST)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data, status=201)
    return Response({}, status=400)


@api_view(["GET"])
def tweet_list_view(request, *args, **kwargs):
    qs = Tweet.objects.all()
    serializer = TweetSerializer(qs, many=True)
    return Response(serializer.data, status=200)


@api_view(["GET"])
def tweet_detail_view(request, tweet_id, *args, **kwargs):
    qs = Tweet.objects.filter(id=tweet_id)
    if not qs:
        return Response({}, status=404)
    serializer = TweetSerializer(qs.first())
    return Response(serializer.data, status=200)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def tweet_delete_view(request, tweet_id, *args, **kwargs):
    qs = Tweet.objects.filter(id=tweet_id)
    if not qs:
        return Response({}, status=404)
    qs = qs.filter(user=request.user)
    if not qs:
        return Response({"message": "You can not delete it"}, status=403)
    obj = qs.first()
    obj.delete()
    return Response({"message": "Tweet deleted"}, status=204)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def tweet_action_view(request, *args, **kwargs):
    serializer = TweetActionSerializer(data=request.POST)
    if serializer.is_valid(raise_exception=True):
        data = serializer.validated_data
        tweet_id = data.get("id")
        action = data.get("action")
        tweet = get_object_or_404(Tweet, id=tweet_id)
        if action == "like":
            tweet.likes.add(request.user)
        elif action == "unlike":
            tweet.likes.remove(request.user)
        elif action == "retweet":
            pass

    return Response({}, status=200)
