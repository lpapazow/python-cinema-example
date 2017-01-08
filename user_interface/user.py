import hashlib
from . import validators


class User(object):
    def __init__(self):
        self.password = None
        self.username = None

    def hash_password(func):
        def decorated(self, password):
            hashed = hashlib.sha1(password.encode('utf-8')).hexdigest()
            return func(self, hashed)
        return decorated

    def validate_password(func):
        def decorated(self, password):
            if not validators.valid_password(password):
                print("Invalid password")
                return False
            return func(self, password)
        return decorated

    @validate_password
    @hash_password
    def set_password(self, password):
        self.password = password
        return True

    def set_username(self, username):
        self.username = username

    @staticmethod
    def hash_string(password):
        return hashlib.sha1(password.encode('utf-8')).hexdigest()


