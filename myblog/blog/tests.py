from django.test import TestCase

from django.contrib.auth.models import User

from blog.forms import ContactForm

from django.core import mail


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

    def test_send_mail(self):
        """Test Contact function."""
        self.client.login(username="testuser1", password="password")
        mail.send_mail(
            "Example subject here",
            "Here is the message body.",
            "from@example.com",
            ["to@example.com"],
        )

        self.assertEqual(len(mail.outbox), 1, "Inbox is not empty")
        self.assertEqual(mail.outbox[0].subject, "Example subject here")
        self.assertEqual(mail.outbox[0].body, "Here is the message body.")
        self.assertEqual(mail.outbox[0].from_email, "from@example.com")
        self.assertEqual(mail.outbox[0].to, ["to@example.com"])


class HomeViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser1", password="password")

    def tearDown(self):
        self.user.delete()

    def test_home_view_not_logged_in_add(self):
        """Tests that not logged in users don't see "Add Blog Post"-option."""
        response = self.client.get("/")
        self.assertNotContains(response, "Add Blog Post")

    def test_home_view_not_logged_in_logout(self):
        """Tests that not logged in users don't see "Logout"-option."""
        response = self.client.get("/")
        self.assertNotContains(response, "Logout")

    def test_home_view_not_logged_in_contact(self):
        """Tests that not logged in users don't see "Contact"-option."""
        response = self.client.get("/")
        self.assertNotContains(response, "Contact")

    def test_home_view_not_logged_in_register(self):
        """Tests that not logged in users don't see "Add Blog Post"-option."""
        response = self.client.get("/")
        self.assertContains(response, "Register")

    def test_home_view_logged_in_add(self):
        """Tests that logged in users see "Add Blog Post"-option."""
        self.client.login(username="testuser1", password="password")
        response = self.client.get("/")
        self.assertContains(response, "Add Blog Post")

    def test_home_view_logged_in_logout(self):
        """Tests that logged in users see "Logout"-option."""
        self.client.login(username="testuser1", password="password")
        response = self.client.get("/")
        self.assertContains(response, "Logout")

    def test_home_view_logged_in_contact(self):
        """Tests that logged in users see "Contact"-option."""
        self.client.login(username="testuser1", password="password")
        response = self.client.get("/")
        self.assertContains(response, "Contact")

    def test_home_view_logged_in_register(self):
        """Tests thatlogged in users see "Register"-option."""
        self.client.login(username="testuser1", password="password")
        response = self.client.get("/")
        self.assertNotContains(response, "Register")
