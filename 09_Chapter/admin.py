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

class Admin(User):
    def __init__(self, first_name, last_name, username, email, location):
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = []

    def list_privileges(self):
        print(f"These are your privileges: ")
        for privilege in self.privileges:
            print(f"- {privilege}")

my_admin = Admin('Jack', 'Spark', 'jack123', 'jack123@email.com', 'Seattle')
my_admin.privileges = ['can add post', 'can delete post', 'can ban user']

my_admin.greet_user()
my_admin.list_privileges()