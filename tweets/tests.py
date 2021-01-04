from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIClient

from .models import Tweet

User = get_user_model()


class TweetTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="Gideon", password="Raven47")
        self.first_tweet = Tweet.objects.create(
            content="For the Emperor!", user=self.user
        )
        self.current_count = Tweet.objects.all().count()

    def get_client(self):
        client = APIClient()
        client.force_login(self.user)

        return client

    def test_tweet_create_view(self):
        client = self.get_client()
        request_data = {"content": "This is second tweet"}
        response = client.post(
            "/api/tweets/create/",
            data=request_data,
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(self.current_count + 1, response.json().get("id"))

    def test_tweets_list_view(self):
        client = self.get_client()
        response = client.get("/api/tweets/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)

    def test_tweets_action_like(self):
        client = self.get_client()
        response = client.post(
            "/api/tweets/action/",
            data={
                "id": 1,
                "action": "like",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get("likes"), 1)

    def test_tweets_action_unlike(self):
        client = self.get_client()
        response = client.post(
            "/api/tweets/action/",
            data={
                "id": 1,
                "action": "like",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get("likes"), 1)

        response = client.post(
            "/api/tweets/action/",
            data={
                "id": 1,
                "action": "unlike",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get("likes"), 0)

    def test_tweets_action_retweet(self):
        client = self.get_client()
        response = client.post(
            "/api/tweets/action/",
            data={
                "id": 1,
                "action": "retweet",
            },
        )

        self.assertEqual(response.status_code, 201)
        self.assertNotEqual(1, response.json().get("id"))

    def test_tweets_detail_view(self):
        client = self.get_client()
        response = client.get("/api/tweets/1/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get("id"), 1)
