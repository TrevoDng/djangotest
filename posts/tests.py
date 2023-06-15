from django.test import TestCase
from django.urls import reverse
from .models import Post
# Create your tests here.

#use: python manage.py startapp appname to create app that comes with tests.py
#or use: python3 manage.py startapp appname if python not working
#then use: python manage.py test posts
# you can chenge text ="value" to see if the test is really working
#if it is working correctly it will fail after using different text= "values".

class PostTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(text="This is a test!")

    def test_model_content(self):
        self.assertEqual(self.post.text, "This is a test!")

    def test_url_exists_at_correct_locals(self):
        response = self.client.get("/posts/")
        self.assertEqual(response.status_code, 200)

    def test_homepage(self):
        response = self.client.get(reverse("posts"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "posts/posts.html")
        self.assertContains(response, "This is a test!")