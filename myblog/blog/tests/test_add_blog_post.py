from django.test import TestCase
from django.contrib.auth.models import User


class SimpleTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            username="testuser", password="password"
        )

    def tearDown(self):
        self.user.delete()

    def test_add_blog_post(self):
        """Test if a blog post created in the admin will show up on the front page."""
        self.client.login(username="testuser", password="password")
        response = self.client.post(
            "/admin/blog/blog/add/",
            {
                "title": "some title",
                "title_tag": "some title",
                # "header_image": "(binary)",
                "body": "some body",
                # "_save": "Save",
            },
        )
        self.assertEqual(response.status_code, 302)
        response = self.client.get("/")
        self.assertTrue("some title" in str(response.content))
