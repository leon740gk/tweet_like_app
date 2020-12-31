from django.http import HttpResponse


def home_page(request, *args, **kwargs):
    return HttpResponse("<h1>Yo! It's home page</h1>")

def tweet_detail_view(request, tweet_id, *args, **kwargs):
    return HttpResponse(f"This is tweet # {tweet_id}")
