from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver
import time
from django.contrib.auth.models import User


class MySeleniumTests(StaticLiveServerTestCase):
    fixtures = []

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)
        cls.user = User.objects.create_user(username="testuser1", password="password")

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_login(self):
        "Test login with selenium."
        self.client.login(username="testuser1", password="password")
        self.selenium.get("%s%s" % (self.live_server_url, "/members/login/"))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys("testuser1")
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys("password")
        self.selenium.find_element_by_id("login-button").click()
        time.sleep(100)
