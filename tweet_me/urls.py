from django.contrib import admin
from django.urls import include, path

from tweets.views import (
    home_page,
    tweet_create_view,
    tweet_detail_view,
    tweet_list_view,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_page),
    path("tweets", tweet_list_view),
    path("create-tweet", tweet_create_view),
    path("tweets/<int:tweet_id>", tweet_detail_view),
    path("api/tweets/", include("tweets.urls")),
]
