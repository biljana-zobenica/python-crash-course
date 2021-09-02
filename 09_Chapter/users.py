class User:
    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
    
    def describe_user (self):
        print(f"{self.first_name} {self.last_name}")
        print(f"Username: {self.username}")
        print(f"E-mail address: {self.email}")
        print(f"Location: {self.location}")

    def greet_user (self):
        print(f"Hello {self.first_name}! Thank you for logging in!")

user_1 = User ('Sophie', 'Stevens', 'soph23', 'soph23@email.com', 'New York')
user_1.describe_user()
user_1.greet_user()

user_2 = User ('James', 'Jackson', 'jamie12', 'jamiej@email.com', 'Chicago')
user_2.describe_user()
user_2.greet_user()
