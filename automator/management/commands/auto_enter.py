# automator/management/commands/auto_enter.py
import random
import string
import time
from django.core.management.base import BaseCommand
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

import time

class Command(BaseCommand):
    help = 'Automatically enters generated usernames and passwords into a website'

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
            for _ in range(count):
                # Generate username and password
                username = generate_username()
                password = generate_password()

                # Find the input fields for username and password
                username_field = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="username"]'))
                )
                password_field = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="password"]'))
                )

                # Clear the fields before entering new credentials
                username_field.clear()
                password_field.clear()

                # Enter the credentials
                username_field.send_keys(username)
                password_field.send_keys(password)

                # Submit the form
                password_field.submit()

                # Wait for the page to load and process the response
                time.sleep(1)

                # Check if the login was successful or not
                if is_login_successful(driver):
                    print(f'Successful login: username={username}, password={password}')
                else:
                    print(f'Login failed: username={username}, password={password}')

        finally:
            # Quit the WebDriver
            driver.quit()


import random


def generate_username():
    adjectives = ['happy', 'brave', 'clever', 'eager', 'kind']
    nouns = ['student', 'teacher', 'parent', 'admin', 'staff']

    adjective = random.choice(adjectives)
    noun = random.choice(nouns)

    username = f"{adjective}_{noun}" and f"{adjective}{noun}"

    # Remove underscore if the username contains 'example'
    if 'example' in username:
        username = username.replace('_', '')

    return username

def generate_password():
    words = ['maktab', 'dars', 'oquv', 'yangilik', 'test']
    numbers = ['123', '456', '789', '2022', '2023']

    word = random.choice(words)
    number = random.choice(numbers)

    return f"{word}{number}"


def generate_credentials():
    username = generate_username()
    password = generate_password()

    return username, password


def is_login_successful(driver):
    # Implement your logic to check if the login was successful
    # For example, you can check for elements on the page after successful login
    return False  # Update this based on your website's login success condition
