# automator/management/commands/auto_enter.py
import random
import string
from django.core.management.base import BaseCommand
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Command(BaseCommand):
    help = 'Automatically enters randomly generated usernames and passwords into a website'

    def add_arguments(self, parser):
        parser.add_argument('url', type=str, help='URL of the website')
        parser.add_argument('count', type=int, help='Number of times to enter the credentials')

    def handle(self, *args, **options):
        url = options['url']
        count = options['count']

        # Configure your Selenium WebDriver here (e.g., ChromeDriver)
        driver = webdriver.Chrome()

        # Navigate to the website
        driver.get(url)

        try:
            # Find the input fields for username and password
            username_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, 'username_field_id'))
            )
            password_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, 'password_field_id'))
            )

            # Enter randomly generated credentials for the specified number of times
            for _ in range(count):
                # Generate random username and password
                username = generate_random_username()
                password = generate_random_password()

                # Clear the fields before entering new credentials
                username_field.clear()
                password_field.clear()

                # Enter the credentials
                username_field.send_keys(username)
                password_field.send_keys(password)

                # Submit the form
                password_field.send_keys(Keys.RETURN)

                # Wait for the page to load
                WebDriverWait(driver, 10).until(EC.title_contains('Success'))

        finally:
            # Quit the WebDriver
            driver.quit()


