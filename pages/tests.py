from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.

#methods steps
#testing if home page url exist at correct location
#use same url("/") used from urls.py
#test url name("home") is available
#test url name("home") is under correct template/folder
#test if our html is in correct format
#note that values you put in double qoutes("") are important
#don't forget we use manage.py to run our test
class HomePageTest(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "pages/home.html")

    def test_template_content(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "<h1>Homepage</h1>")
        self.assertNotContains(response, "Not on the page")


class AboutPageTest(SimpleTestCase):
    def test_url_exist_at_correct_location(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("about"))
        self.assertTemplateUsed(response, "pages/about.html")

    def test_template_content(self):
        response = self.client.get(reverse("about"))
        self.assertContains(response, "<h1>About page</h1>")
        self.assertNotContains(response, "Should not be here!")