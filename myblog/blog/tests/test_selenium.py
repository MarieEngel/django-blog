import os

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth.models import User
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SeleniumTest(StaticLiveServerTestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        if os.getenv("CI"):
            options.binary_location = "/usr/bin/google-chrome-stable"
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
            self.driver = webdriver.Chrome(options=options)
        else:
            from chromedriver_binary import chromedriver_filename

            self.driver = webdriver.Chrome(chromedriver_filename, options=options)
        self.user = User.objects.create_user(username="testuser1", password="password")

    def tearDown(self):
        self.user.delete()

    def test_add_blog_post(self):
        """Tests excistence blog post form."""
        self.driver.get(f"{self.live_server_url}/members/login/")
        username_field = self.driver.find_element_by_name("username")
        username_field.send_keys("testuser1")
        password_field = self.driver.find_element_by_name("password")
        password_field.send_keys("password")
        login_button = self.driver.find_element_by_id("login-button")
        login_button.click()
        add_blog_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.CSS_SELECTOR,
                    "#navbarSupportedContent > ul > li:nth-child(1) > a",
                )
            )
        )
        add_blog_button.click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "id_title"))
        )
        title_fields = self.driver.find_elements_by_css_selector("#id_title")
        self.assertEqual(len(title_fields), 1)

    def test_register_username(self):
        """Tests if username field exists for registration."""
        self.driver.get(f"{self.live_server_url}/")
        register_button = self.driver.find_element_by_css_selector(
            "#navbarSupportedContent > ul > li:nth-child(1) > a"
        )
        register_button.click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "id_username"))
        )
        username_fields = self.driver.find_elements_by_id("id_username")
        self.assertEqual(len(username_fields), 1)

    def test_register_password(self):
        """Tests if password field exists for registration."""
        self.driver.get(f"{self.live_server_url}/")
        register_button = self.driver.find_element_by_css_selector(
            "#navbarSupportedContent > ul > li:nth-child(1) > a"
        )
        register_button.click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "id_password1"))
        )
        password_fields = self.driver.find_elements_by_id("id_password1")
        self.assertEqual(len(password_fields), 1)

    def test_register_register(self):
        """Tests redirection to login after registration."""
        self.driver.get(f"{self.live_server_url}/members/register/")
        username_field = self.driver.find_element_by_id("id_username")
        username_field.send_keys("testuser4")
        password_field = self.driver.find_element_by_id("id_password1")
        password_field.send_keys("newsecret")
        password_field = self.driver.find_element_by_id("id_password2")
        password_field.send_keys("newsecret")
        register_button = self.driver.find_element_by_xpath(
            "/html/body/div/div/form/button"
        )
        register_button.click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="login-button"]'))
        )
        self.assertIn("/members/login/", self.driver.current_url)
