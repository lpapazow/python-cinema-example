import re


def valid_password(password):
    if len(password) < 8:
        return False
    special_char = re.compile("[\@\!\#\$\%\^\&\*\(\)\-\_]")
    if not special_char.search(password):
        return False
    capital = re.compile("[A-Z]")
    if not capital.search(password):
        return False
    return True
