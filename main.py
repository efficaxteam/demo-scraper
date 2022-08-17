"""Entry module for the application.

Creates some fake credentials and registers a new account with core.register method.
"""
from random import randint

from faker import Faker
from selenium import webdriver

import core


def main():
    """Entry point for the application."""
    driver = webdriver.Chrome()

    fake = Faker()

    fake_profile_name = fake.profile('name')
    fake_profile_username = fake.profile('username')

    fullname = fake_profile_name.get('name').split()
    username = f"{fake_profile_username.get('username')}{randint(100, 999)}"
    password = fake.password()
    birth_year = randint(1950, 2000)

    core.register(driver=driver, firstname=fullname[0], lastname=fullname[1], username=username, password=password,
                  birth_year=birth_year)


if __name__ == "__main__":
    main()
