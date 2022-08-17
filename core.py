"""Core module for the project.

This script allows the admin to manage WebDriver instances.

Avaliable methods:
    * register - creates a new Yahoo account.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import constants as const
import phone_activate


def register(driver: WebDriver,
             firstname: str,
             lastname: str,
             username: str,
             password: str,
             birth_year: int) -> bool:
    """Creates a new Yahoo account.

    :param driver: WebDriver instance.
    :param firstname: First name of the user.
    :param lastname: Last name of the user.
    :param username: Username of the user.
    :param password: Password of the user.
    :param birth_year: Birth year of the user.
    :returns: True if the account was created, False otherwise.
    """
    driver.get(const.YAHOO_REGISTER_URL)
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, const.REG_FIRSTNAME_INPUT_XPATH))
        )
        element.send_keys(firstname)

    except Exception as e:
        return False

    driver.find_element(By.XPATH, const.REG_LASTNAME_INPUT_XPATH).send_keys(lastname)
    driver.find_element(By.XPATH, const.REG_USERNAME_INPUT_XPATH).send_keys(username)
    driver.find_element(By.XPATH, const.REG_PASSWORD_INPUT_XPATH).send_keys(password)
    driver.find_element(By.XPATH, const.REG_BIRTH_YEAR_INPUT_XPATH).send_keys(birth_year)
    driver.find_element(By.XPATH, const.REG_SUBMIT_BUTTON_XPATH).click()

    phone_number = phone_activate.get_phone_number()

    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, const.REG_PHONE_INPUT_XPATH))
        )
        element.send_keys(phone_number)

    except Exception as e:
        return False

    driver.find_element(By.XPATH, const.REG_SEND_CODE_BUTTON_XPATH).click()

    # Since it's a demo project, we don't implement captcha bypass.

    code = phone_activate.get_code()

    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, const.REG_CODE_INPUT_XPATH))
        )
        element.send_keys(code)

    except Exception as e:
        return False

    driver.find_element(By.XPATH, const.REG_VERIFY_CODE_BUTTON_XPATH).click()

    return True
