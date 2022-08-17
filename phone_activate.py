"""Module for getting/activating phone number.

Since it's a demo project we will use a phone number and code from input prompt.
"""


def get_phone_number(prefix: str = None) -> str:
    """Get phone number from user.
    :param prefix: Prefix for the phone number. Looks like +380, +33, etc.
    """
    return input(f"Enter phone number: {prefix or ''} ")


def get_code():
    """Get code from user.
    """
    return input("Enter code: ")
