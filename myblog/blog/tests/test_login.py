from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver


class MySeleniumTests(StaticLiveServerTestCase):
    fixtures = []

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_login(self):
        self.selenium.get("%s%s" % (self.live_server_url, "/members/login/"))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys("myuser")
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys("secret")
        self.selenium.find_element_by_id("login-button").click()
