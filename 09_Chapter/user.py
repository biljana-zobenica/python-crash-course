"""A class for modeling users."""

class User:
    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0
    
    def describe_user (self):
        print(f"{self.first_name} {self.last_name}")
        print(f"Username: {self.username}")
        print(f"E-mail address: {self.email}")
        print(f"Location: {self.location}")

    def greet_user (self):
        print(f"Hello {self.first_name}! Thank you for logging in!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0