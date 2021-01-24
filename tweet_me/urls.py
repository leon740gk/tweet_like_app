from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

from tweets.views import (
    home_page,
    tweet_create_view,
    tweet_detail_view,
    tweet_list_view,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_page),
    path("react/", TemplateView.as_view(template_name="react_via_js.html")),
    path("tweets", tweet_list_view),
    path("create-tweet", tweet_create_view),
    path("tweets/<int:tweet_id>", tweet_detail_view),
    path("api/tweets/", include("tweets.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
