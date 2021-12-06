from django.test import TestCase

from django.contrib.auth.models import User

from blog.forms import ContactForm

# Create your tests here.
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


class ContactFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser1", password="password")

    def tearDown(self):
        self.user.delete()

    def test_invalid_form_valid(self):
        """Tests valid input into the contact form."""
        self.client.login(username="testuser1", password="password")
        data = {
            "name": "some name",
            "email": "some@email.berlin",
            "subject": "some subject",
            "message": "some message",
        }
        form = ContactForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form_invalid(self):
        """Tests invalid input into the contact form."""
        self.client.login(username="testuser1", password="password")
        data = {
            "name": "Some name",
            "email": "",
            "subject": "Missing message",
            "message": "",
        }
        form = ContactForm(data=data)
        self.assertFalse(form.is_valid())
