"""A collection of classes for modeling an admin user account."""

from user import User

class Admin(User):
    def __init__(self, first_name, last_name, username, email, location):
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = Privileges()

class Privileges():
    def __init__(self, privileges= []):
        self.privileges = privileges

    def list_privileges(self):
        if self.privileges:
            print(f"These are your privileges: ")
            for privilege in self.privileges:   
                print(f"- {privilege}")
        else:
            print(f"User doesn't have privileges.")

