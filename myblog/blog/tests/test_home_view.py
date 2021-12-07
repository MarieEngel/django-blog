from django.test import TestCase
from django.contrib.auth.models import User


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
