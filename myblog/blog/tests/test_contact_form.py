from django.core import mail
from django.test import TestCase
from django.contrib.auth.models import User
from blog.forms import ContactForm


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
